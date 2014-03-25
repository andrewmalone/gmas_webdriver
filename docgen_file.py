import inspect
import importlib
import re

template = """
{classdoc}

{descriptors}
{methods}"""

subclass_template = """{descriptors}{methods}"""

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

method_subtemplate = """
**{methodname}**{methodargs}

>>{methoddoc}
"""

descriptor_subtemplate = """
**{descriptor_name}**

>>{descriptor_doc}
"""

classname = ""

def get_class(meth):
    for cls in inspect.getmro(meth.im_class):
        if meth.__name__ in cls.__dict__:
            return cls.__name__
    return None

def get_method_list(class_name):
    cls = getattr(importlib.import_module("pages.%s" % (class_name)), class_name)
    global classname
    classname = cls
    return get_methods(cls)

def get_methods(cls, subclass=False):
    # cls = getattr(importlib.import_module("pages.%s" % (class_name)), class_name)
    lookup = {}
    lookup["classname"] = cls.__name__
    if subclass is False:
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
            if subclass is True:
                lookup["methods"] += method_subtemplate.format(**m_lookup)
            else: lookup["methods"] += method_template.format(**m_lookup)

    # list of descriptors
    for obj in sorted(cls.__dict__):
        d_lookup = {}
        if inspect.isdatadescriptor(cls.__dict__[obj]):
            o = cls.__dict__[obj]
            d_lookup["descriptor_name"] = obj
            d_lookup["descriptor_doc"] = escape(inspect.getdoc(o))
            if subclass is True:
                lookup["descriptors"] += descriptor_subtemplate.format(**d_lookup)
            else: lookup["descriptors"] += descriptor_template.format(**d_lookup)

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
    find = re.compile(r'^//([^\s]*).*$', re.MULTILINE)
    def repl(matchobj):
        cls = matchobj.group(1)
        return escape(get_methods(classname.__dict__[cls], True))
    return re.sub(find, repl, string)

if __name__ == "__main__":
    #scr = raw_input("Screen: ")
    #padding = '000'
    #num = re.match(r'[0-9]{1,3}', scr).group(0)
    #scr = "SCR%s%s" % (padding[:4 - len(num)], scr)
    print get_method_list("SCR0344")

