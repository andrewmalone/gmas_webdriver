from gmas_webdriver.pages.Page import Page
import inspect
from datetime import datetime


class wrapper(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __getattr__(self, attr):
        """
        overrides tohe default getter. Used for getting page object attributes or calling
        page object methods
        """
        # get the desired attributes from each page object
        a = getattr(self._a, attr)
        b = getattr(self._b, attr)

        if callable(a) and callable(b):
            # attr is a method, so we need to call it and return the result
            self._attr = attr
            return self.call

        # check if this is a builtin type, if so return the attribute directly
        if (a.__class__.__module__ == '__builtin__' and b.__class__.__module__ == '__builtin__') or (a.__class__.__module__ == 'pages.elements' and b.__class__.__module__ == 'pages.elements'):
            if a == b:
                return a
            else:
                return 0

        # need to return a wrapper object if not a builtin
        # this is used for any sub objects that are GMWebElements or
        # something else(like rows within a page object)
        return wrapper(a, b)

    def __setattr__(self, attr, value):
        """
        overrides the default setter
        """
        if attr[0] == '_':
            # underscore prefixed attributes are internal to the wrapper object, not the
            # wrapped objects, so we can set them directly
            self.__dict__[attr] = value
        else:
            # set the attributes in the wrapped objects
            if hasattr(self._a, attr):
                # check for returnObj and random
                element = getattr(self._a, attr)
                if value == "random" and element.__class__.__name__ == "returnObj" and element.options != "":
                    # get the options
                    import random
                    value = random.choice(element.options)
                self._a.__setattr__(attr, value)
            if hasattr(self._b, attr):
                self._b.__setattr__(attr, value)

    def call(self, *args, **kwargs):
        """
        call function calls methods on each wrapped page object
        """
        a = getattr(self._a, self._attr)(*args, **kwargs)
        b = getattr(self._b, self._attr)(*args, **kwargs)

        # check if we are getting a page object
        if isinstance(a, Page) and isinstance(b, Page):
            self._a = a
            self._b = b
            return self

        # check if this is a builtin type
        if a.__class__.__module__ == '__builtin__' and b.__class__.__module__ == '__builtin__':
            if a == b:
                return a
            else:
                return 0

        # need to return a wrapper object if not a Page or builtin
        return wrapper(a, b)

    def compare(self, formats={}):
        a = get_properties(self._a)
        b = get_properties(self._b)
        compare_properties(a, b, formats=formats)


def get_properties(object):
    """
    Gets properties for a page object, returns a dictionary
    """
    properties = {}
    # exclude some properties that we don't need to compare
    exclusions = [
        "env",
        "env_url",
        "mode",
        "scr",
        "locators",
        "_locators",
        "page_title"
    ]
    for name, member in inspect.getmembers(object, lambda a: not(inspect.isroutine(a))):
        if name[:2] == "__" or member.__class__.__module__ != '__builtin__' or type(member) is type or name in exclusions:
            continue
        attr = getattr(object, name)
        if type(attr) is list:
            properties[name] = []
            for i, item in enumerate(attr):
                properties[name].append(get_properties(item))
        else:
            properties[name] = attr
    return properties


def compare_properties(a, b, formats={}, parent=None, index=None):
    """
    Compare two dictionaries of properties
    """
    format_funcs = {
        "date": date_format,
        "percent": percent_format
    }
    for name, val_a in a.iteritems():
        try:
            val_b = b[name]
        except:
            val_b = None
        if type(val_a) is list:
            for i, item in enumerate(val_a):
                try:
                    vb = val_b[i]
                except:
                    vb = None
                compare_properties(item, vb, parent=name, index=i, formats=formats)
            # check if b has extra rows
            for i, item in enumerate(val_b[len(val_a):]):
                print "False {}[{}] not in a".format(name, i)
        else:
            n = name
            if parent is not None:
                n = "{}.{}".format(parent, name)
            if n in formats:
                if callable(formats[n]):
                    format_func = formats[n]
                else:
                    format_func = format_funcs[formats[n]]
                val_a_new = format_func(val_a)
                compare = val_a_new == val_b
                val_a = "{} => {}".format(val_a, val_a_new)
            else:
                compare = val_a == val_b
            if parent is not None and index is not None:
                name = "{}[{}].{}".format(parent, index, name)
            # check the values
            print "{} {}: ({}, {})".format(compare, name, val_a, val_b)


def date_format(string):
    if string == "":
        return string
    d = datetime.strptime(string, "%m-%d-%Y")
    d2 = "{dt:%b} {dt.day}, {dt.year}".format(dt=d)
    return d2


def percent_format(string):
    if string == "":
        return string
    return string.rstrip("0").rstrip(".") + "%"
