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


def get_class(meth):
    for cls in inspect.getmro(meth.im_class):
        if meth.__name__ in cls.__dict__:
            return cls.__name__
    return None


def get_method_list(class_name):
    cls = getattr(importlib.import_module("pages.%s" % (class_name)), class_name)
    lookup = {}
    lookup["classname"] = cls.__name__
    lookup["classdoc"] = escape(inspect.getdoc(cls))
    lookup["methods"] = ""
    lookup["descriptors"] = ""
    # list of methods...
    for meth in inspect.getmembers(cls, inspect.ismethod):
        m_lookup = {}
        m = meth[1]
        if get_class(m) != "Page" and get_class(m) != "GMWebElement" and m.__name__[0] != "_":
            name = m.__name__
            #print name
            args = inspect.formatargspec(*inspect.getargspec(m))
            args = args.replace("self, ", "").replace("self", "")
            # print "%s%s" % (name, args)
            m_lookup["methodname"] = name
            m_lookup["methodargs"] = args
            find = r'SCR_([0-9]{4}[a-z]?)'
            repl = r'[SCR_\1](SCR\1)'
            m_lookup["methoddoc"] = escape(re.sub(find, repl, inspect.getdoc(m)))
            lookup["methods"] += method_template.format(**m_lookup)

    # list of descriptors
    for obj in sorted(cls.__dict__):
        d_lookup = {}
        if inspect.isdatadescriptor(cls.__dict__[obj]):
            o = cls.__dict__[obj]
            d_lookup["descriptor_name"] = obj
            d_lookup["descriptor_doc"] = escape(inspect.getdoc(o))
            lookup["descriptors"] += descriptor_template.format(**d_lookup)

    # TODO: add in getting doc strings from internal classes

    # Add some headers
    if lookup["methods"] != "":
        lookup["methods"] = method_header + lookup["methods"]
    if lookup["descriptors"] != "":
        lookup["descriptors"] = descriptor_header + lookup["descriptors"]

    return template.format(**lookup)

def escape(string):
    return string.replace("<", "\<").replace("\n\n","\n>\n").replace("\n", "  \n")

print get_method_list(scr)

