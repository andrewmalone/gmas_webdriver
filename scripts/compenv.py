"""
compenv.py

implements a wrapper class that can be used to compare two different GMAS environments
"""
from pages.Page import Page
import os
import csv


class wrapper(object):
    def __init__(self, a, b, log_folder="", e=0, log=None, compare=True, skip=0, ignore=[]):
        self._a = a
        self._b = b

        # internal var to allow skipping comparisons
        self._skip = skip

        # internal ignore to filter out extra page differences
        if type(ignore) is list:
            self._ignore = {
                "ignore": ignore,
                "ids": []
            }
        else:
            self._ignore = ignore

        # internal var for error tracking
        self._e = e

        # log file header
        if log is None:
            self._log = [['Match', 'Error', 'Page1', 'URL1', 'Page2', 'URL2', 'Pageload1 (ms)', 'Pageload2 (ms)', 'Pageload compare']]
        else:
            self._log = log

        # set up the log folder, adding trailing slash if necessary
        if log_folder != "" and log is None:
                if log_folder[-1] != "/":
                    log_folder = log_folder + "/"
                os.makedirs(log_folder)
        self._log_folder = log_folder

        self._compare = compare

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
        return wrapper(a, b, log_folder = self._log_folder, e = self._e, log = self._log, compare=self._compare, skip=self._skip, ignore=self._ignore)

        
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

            if self._compare is True and self._skip == 0:
                match = "True"
                error = ""

                source1 = self.clean_source(self._a.driver.page_source)
                source2 = self.clean_source(self._b.driver.page_source)

                # use the ignore id list to replace ids
                for ids in self._ignore["ids"]:
                    source1 = source1.replace(ids[0], ids[1])

                # compare the source
                if source1 != source2:
                    # increment the error count
                    self._e += 1
                    match = "False"
                    error = "E%s" % self._e

                    # save the full page sources
                    #self.save_file("E%s-S1.txt" % self._e, self._a.driver.page_source.encode('utf-8'))
                    #self.save_file("E%s-S2.txt" % self._e, self._b.driver.page_source.encode('utf-8'))

                    # save screenshots
                    #self._a.driver.save_screenshot("%sE%s-S1.png" % (self._log_folder, self._e))
                    #self._b.driver.save_screenshot("%sE%s-S2.png" % (self._log_folder, self._e))

                    # do the diff and save to a file
                    import difflib
                    fromfile = self.get_context(self._a)
                    tofile = self.get_context(self._b)
                    result = list(difflib.unified_diff(source1.splitlines(1), source2.splitlines(1), fromfile=fromfile, tofile=tofile))
                    self.save_file("E%s-D.txt" % self._e, result)
            else:
                match = "N/A"
                error = ""

            if self._skip > 0:
                self._skip = self._skip - 1

            load_a = self._a.get_page_load_time()
            load_b = self._b.get_page_load_time()

            log_line = [
                match,
                error,
                self._a.get_current_page(),
                self._a.driver.current_url,
                self._b.get_current_page(),
                self._b.driver.current_url,
                load_a,
                load_b,
                round(float(load_b) / load_a, 2)
            ]
            self._log.append(log_line)
            return self

        # check if this is a builtin type
        if a.__class__.__module__ == '__builtin__' and b.__class__.__module__ == '__builtin__':
            if a == b:
                return a
            else:
                return 0

        # need to return a wrapper object if not a Page or builtin
        return wrapper(a, b, log_folder=self._log_folder, e=self._e, log=self._log, compare=self._compare, skip=self._skip, ignore=self._ignore)

    def clean_source(self, source):
        import re
        # remove all attributes from inside html tags
        source = re.sub(r'<([^/][a-zA-Z]*)\s?[^>]*>', r'<\1>', source)
        # remove instance header/footer
        source = re.sub(r'<font>(G[^<]*)</font>', r'<font></font>', source)
        # remove build tag in footer
        source = re.sub(r'<td>\xa9[^<]*</td>', r'<td></td>', source)
        # remove submitTime javascript
        source = re.sub(r'submitTime = [0-9]*;', r'', source)
        # remove newlines (maybe not needed?)
        # source = re.sub(r'^\n', r'', source, flags=re.MULTILINE)
        # collapse whitespace at the beginning of lines
        source = re.sub(r'^\s*', r'', source, flags=re.MULTILINE)
        if "project id" in self._ignore["ignore"]:
            source = re.sub(r'[0-9]{8}-[0-9]{2}', r'', source)

        return source

    def save_file(self, file, s):
        f = open("%s%s" % (self._log_folder, file), "w")
        if type(s) is list:
            for line in s:
                f.write(line.encode('utf-8'))
        else:
            f.write(s)
        f.close()

    def get_context(self, p):
        """
        return a string with environment/page information
        format is:
        gmasdev.cadm SCR0105jlknv
        segmentId:1234
        noticeId:6434
        """
        s = []
        s.append("%s %s" % (p.env, p.get_current_page()))
        ids = []
        # p is a page object

        # fill in the input values
        inputs = p.find_elements("css=input[type='hidden'][name$='Id']")
        for e in inputs:
            name = e.get_attribute("name")
            idval = e.get_attribute("value")
            if name not in ids and idval != "":
                ids.append(name)
                s.append("%s: %s" % (name, idval))

        return '\n'.join(s)

    def write_log(self, filename="log.csv"):
        with open("%s%s" % (self._log_folder, filename), "wb") as f:
            writer = csv.writer(f)
            writer.writerows(self._log)

    def skip(self, number=1):
        self._skip = number

    def add_log(self, text):
        self._log[-1].append(text)

    def add_ids(self, id_name):
        for ids in zip(self._a.get_ids(id_name), self._b.get_ids(id_name)):
            self._ignore["ids"].append(ids)
