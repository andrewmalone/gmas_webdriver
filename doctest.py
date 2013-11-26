import inspect
import importlib
import re

scr = raw_input("Screen: ")
padding = '000'
num = re.match(r'[0-9]{1,3}', scr).group(0)
scr = "SCR%s%s" % (padding[:4 - len(num)], scr)
print scr

template = """
{classname} Page Object

h1. {classname}
{classdoc}

h2. Descriptors
{descriptors}

h2. Methods
{methods}
"""

method_template = """
h4. {methodname}
{{indent}}
{methoddoc}
{{indent}}
"""

descriptor_template = """
h4. {descriptor_name}
{{indent}}
{descriptor_doc}
{{indent}}
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
    lookup["classdoc"] = inspect.getdoc(cls)
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
            #print "%s%s" % (name, args)
            m_lookup["methodname"] = name + args
            find = r'SCR_([0-9]{4}[a-z]?)'

            repl = r'[SCR_\1|SCR\1 Page Object]'
            m_lookup["methoddoc"] = re.sub(find, repl, inspect.getdoc(m))
            lookup["methods"] += method_template.format(**m_lookup)

    # list of descriptors
    for obj in sorted(cls.__dict__):
        print obj, type(obj)
        d_lookup = {}
        if inspect.isdatadescriptor(cls.__dict__[obj]):
            o = cls.__dict__[obj]
            d_lookup["descriptor_name"] = obj
            d_lookup["descriptor_doc"] = inspect.getdoc(o)
            lookup["descriptors"] += descriptor_template.format(**d_lookup)

    # TODO: add in getting doc strings from internal classes

    print template.format(**lookup)

get_method_list(scr)

