import inspect
import importlib
import re

scr = raw_input("Screen: ")
padding = '000'
num = re.match(r'[0-9]{1,3}', scr).group(0)
scr = "SCR%s%s" % (padding[:4 - len(num)], scr)

template = """
{classname} Page Object

{classdoc}

{descriptors}
{methods}
{subclasses}
"""

subclass_template = """
{descriptors}
{methods}
"""

method_header = "### Methods"
descriptor_header = "### Descriptors"

method_template = """
**{methodname}**{methodargs}

>{methoddoc}
"""

descriptor_template = """
**{descriptor_name}**

>{descriptor_doc}
"""

classname = ""

def get_class(meth):
    for cls in inspect.getmro(meth.im_class):
        if meth.__name__ in cls.__dict__:
            return cls.__name__
    return None


def get_method_list(class_name):
    page_name = "pages.{}".format(class_name)
    cls = getattr(importlib.import_module(page_name), class_name)
    global classname
    classname = cls
    print classname
    return get_methods(cls)

def get_methods(cls, subclass=False):
    # cls = getattr(importlib.import_module("pages.%s" % (class_name)), class_name)
    lookup = {}
    lookup["classname"] = cls.__name__
    lookup["classdoc"] = escape(inspect.getdoc(cls))
    lookup["methods"] = ""
    lookup["descriptors"] = ""
    lookup["subclasses"] = ""

    for meth in inspect.getmembers(cls, inspect.ismethod):
        m_lookup = {}
        m = meth[1]
        if get_class(m) != "Page" and get_class(m) != "GMWebElement" and m.__name__[0] != "_":
            name = m.__name__
            args = inspect.formatargspec(*inspect.getargspec(m))
            args = args.replace("self, ", "").replace("self", "")
            m_lookup["methodname"] = name
            m_lookup["methodargs"] = args

            doc = escape(replace_screen(inspect.getdoc(m)))
            doc = replace_subclass(doc)

            m_lookup["methoddoc"] = doc
            lookup["methods"] += method_template.format(**m_lookup)

    # list of descriptors
    for obj in sorted(cls.__dict__):
        d_lookup = {}
        if inspect.isdatadescriptor(cls.__dict__[obj]):
            o = cls.__dict__[obj]
            d_lookup["descriptor_name"] = obj
            d_lookup["descriptor_doc"] = escape(inspect.getdoc(o))
            lookup["descriptors"] += descriptor_template.format(**d_lookup)

    # Add some headers
    if lookup["methods"] != "":
        lookup["methods"] = ("%s" % ("#" if subclass is True else "")) + method_header + lookup["methods"]
    if lookup["descriptors"] != "":
        lookup["descriptors"] = ("%s" % ("#" if subclass is True else "")) + descriptor_header + lookup["descriptors"]

    if subclass is True:
        return subclass_template.format(**lookup)
    return template.format(**lookup)

def escape(string):
    return string.replace("<", "\<").replace("\n\n","\n>\n").replace("\n", "  \n")

def replace_screen(string):
    find = r'SCR_([0-9]{4}[a-z]?)'
    repl = r'[SCR_\1](SCR\1)'
    return re.sub(find, repl, string)

def replace_subclass(string):
    find = re.compile(r'^//(.*)$', re.MULTILINE)
    def repl(matchobj):
        cls = matchobj.group(1)
        return escape(get_methods(classname.__dict__[cls], True)).replace("\n>  \n","\n>>  \n")
    return re.sub(find, repl, string)

print get_method_list(scr)
