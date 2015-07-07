from gmas_webdriver.pages.Page import Page
import inspect
from datetime import datetime
import csv


class wrapper(object):
    """
    Wrapper class for running parallel tests for jsf conversion
    """
    def __init__(self, a, b, log=None):
        self._a = a
        self._b = b
        if log is None:
            self._log = [["Screen", "URLS", "URL A", "URL B", "Result"]]
        else:
            self._log = log

    def __getattr__(self, attr):
        """
        overrides the default getter. Used for getting page object attributes or calling
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
        return wrapper(a, b, self._log)

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
        return wrapper(a, b, self._log)

    def add_to_log(self, item):
        """
        Adds to the internal log (should be a list for better csv output)
        """
        self._log.append(item)

    def write_log(self, filename="log.csv"):
        """
        Write the comparison log to a csv file
        """
        with open(filename, "wb") as f:
            writer = csv.writer(f)
            for row in self._log:
                writer.writerow([r.encode('ascii', 'xmlcharrefreplace') if isinstance(r, unicode) else r for r in row])

    def compare(self, formats={}):
        """
        Compare all the readable properties of two page objects
        """
        a = get_properties(self._a)
        b = get_properties(self._b)
        load_a = self._a.get_page_load_time()
        load_a_detail = self._a.get_page_load_details()
        load_b = self._b.get_page_load_time()
        load_b_detail = self._b.get_page_load_details()
        perf = round(float(load_b) / load_a, 2)
        # print "Performance: {} ({},{})".format(perf, load_a, load_b)
        urls = "* [GDEV|{}]\n* [GSAND|{}]".format(self._a.driver.current_url, self._b.driver.current_url)
        self.add_to_log([self._a.scr, urls, self._a.driver.current_url, self._b.driver.current_url, "Performance", load_a, load_a_detail, load_b, load_b_detail, perf])
        prefix = [self._a.scr, urls, self._a.driver.current_url, self._b.driver.current_url]
        results = compare_properties(a, b, formats=formats)
        for result in results:
            # print result
            # print prefix + result
            self.add_to_log(prefix + result)


def get_properties(object):
    """
    Gets properties for a page object, returns a dictionary
    """
    page_module = object.__class__.__module__
    # print page_module
    properties = {}
    # exclude some properties that we don't need to compare
    exclusions = [
        "env",
        "env_url",
        "mode",
        "scr",
        "locators",
        "_locators",
        "page_title",
        "page"
    ]
    for name, member in inspect.getmembers(object, lambda a: not(inspect.isroutine(a))):
        module = member.__class__.__module__
        # print name, member, module
        if name[:2] == "__" or (module != '__builtin__' and module != page_module) or type(member) is type or name in exclusions:
            # print "Excluded"
            continue
        attr = getattr(object, name)
        if type(attr) is list:
            properties[name] = []
            for i, item in enumerate(attr):
                properties[name].append(get_properties(item))
        elif module == page_module:
            properties[name] = get_properties(attr)
        else:
            properties[name] = attr
    return properties


def test_properties(object, parent=None, index=None):
        """
        Gets properties for a page object, returns a dictionary
        """
        page_module = object.__class__.__module__
        # properties = {}
        # exclude some properties that we don't need to compare
        exclusions = [
            "env",
            "env_url",
            "mode",
            "scr",
            "locators",
            "_locators",
            "page_title",
            "page"
        ]
        for name, member in inspect.getmembers(object, lambda a: not(inspect.isroutine(a))):
            module = member.__class__.__module__
            # print name, member, module
            if name[:2] == "__" or (module != '__builtin__' and module != page_module and module != "pages.elements") or type(member) is type or name in exclusions:
                # if name[:2] == "__":
                #     print "Excluded name=__"
                # if (module != '__builtin__' and module != page_module):
                #     print "Excluded module"
                # if type(member) is type:
                #     print "Excluded type"
                # if name in exclusions:
                #     print "Excluded ex"
                continue
            # print name
            attr = getattr(object, name)
            if type(attr) is list:
                # properties[name] = []
                for i, item in enumerate(attr):
                    # properties[name].append(get_properties(item))
                    test_properties(item, parent=name, index=i)
            elif module == page_module:
                # properties[name] = get_properties(attr)
                # print "module?", name
                test_properties(attr, parent=name)
            else:
                if parent is not None and index is not None:
                    name = "{}[{}].{}".format(parent, index, name)
                if parent is not None and index is None:
                    name = "{}.{}".format(parent, name)
                # properties[name] = attr
                # print attr is None, attr == None
                try:
                    print "{}: {}".format(name, "ELEMENT NOT FOUND" if attr is None else attr)
                except UnicodeError:
                    print "{}: {}".format(name, "ELEMENT NOT FOUND" if attr is None else attr.encode('ascii', 'xmlcharrefreplace'))
        # return properties


def compare_properties(a, b, formats={}, parent=None, index=None, results=None):
    """
    Compare two dictionaries of properties
    """
    # print results
    if results is None:
        results = []
    format_funcs = {
        "date": date_format,
        "percent": percent_format,
        "dollar": dollar_format,
        "name": name_format,
        "case": sentence_case_format
    }
    for name, val_a in a.iteritems():
        #print name, type(val_a)
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
                results = compare_properties(item, vb, parent=name, index=i, formats=formats, results=results)
            # check if b has extra rows
            for i, item in enumerate(val_b[len(val_a):]):
                # print "False {}[{}] not in a".format(name, i)
                # results.append(["False {}[{}] not in a".format(name, i)])
                results.append([False, "{}[{}] not in a".format(name, i)])
        elif type(val_a) is dict:
            results = compare_properties(val_a, val_b, parent=name, formats=formats, results=results)
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
                try:
                    val_a = "{} => {}".format(val_a, val_a_new)
                except UnicodeEncodeError:
                    val_a = u"{} => {}".format(val_a, val_a_new)
            else:
                compare = val_a == val_b
            if parent is not None and index is not None:
                name = "{}[{}].{}".format(parent, index, name)
            if parent is not None and index is None:
                name = "{}.{}".format(parent, name)
            # check the values
            # print "{} {}: ({}, {})".format(compare, name, val_a, val_b)
            # s = "{} {}: ({}, {})".format(compare, name, val_a, val_b)
            s = [compare, name, val_a, val_b]
            # print s
            results.append(s)
    return results


def date_format(string, fmt="%m-%d-%Y"):
    if string == "" or string is None:
        return string
    d = datetime.strptime(string, fmt)
    d2 = "{dt:%b} {dt.day}, {dt.year}".format(dt=d)
    return d2


def percent_format(string):
    if string == "":
        return string
    if "." in string:
        string = string.rstrip("0").rstrip(".")
    return string + "%"


def dollar_format(string):
    negative = False
    if string == "" or string == "None" or string == "NONE" or string is None:
        return string
    if string[0] == "(" and string[-1] == ")":
        negative = True
        string = string[1:-1]
    if string[-3:] == ".00":
        string = string[:-3]
    if string[0] != "$":
        string = "$" + string
    if negative:
        string = "(" + string + ")"
    return string


def name_format(string):
    if string == "" or string is None:
        return string
    names = string.split(",")
    first_name = names[1].strip()
    last_name = names[0].strip()
    if " " in first_name:
        first_name = first_name.split(" ")[0]
    return first_name + " " + last_name


def sentence_case_format(string):
    if string == "" or string is None:
        return string
    return " ".join([word if i == 0 else word.lower() for i, word in enumerate(string.split(" "))])
