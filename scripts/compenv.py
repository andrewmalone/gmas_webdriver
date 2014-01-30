class wrapper(object):
    # @todo - add log file locations
    # @todo - add performance profile on page load
    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._e = 0

    def __getattr__(self, attr):
        def empty():
            return None
        a = getattr(self._a, attr)
        b = getattr(self._b, attr)
        if callable(a) and callable(b):
            self._attr = attr
            return self.call

        # check if this is a builtin type
        if a.__class__.__module__ == '__builtin__' and b.__class__.__module__ == '__builtin__':
            if a == b:
                return a
            else: return 0

        # need to return a wrapper object if not a builtin
        return wrapper(a, b)
        # need to return the actual attribute if this is getting data (not sure how yet)
        # example: project snapshot, documents, etc...
        
    def __setattr__(self, attr, value):
        if attr[0] == '_':
            self.__dict__[attr] = value
        else:
            # print "set %s to %s" % (attr, value)
            if hasattr(self._a, attr):
                self._a.__setattr__(attr, value)
            if hasattr(self._a, attr):
                self._b.__setattr__(attr, value)

    def call(self, *args):
        a = getattr(self._a, self._attr)(*args)
        b = getattr(self._b, self._attr)(*args)

        # check if we are getting a page object
        from pages.Page import Page
        if isinstance(a, Page) and isinstance(b, Page):
            self._a = a
            self._b = b

            source1 = self.clean_source(self._a.driver.page_source)
            source2 = self.clean_source(self._b.driver.page_source)

            # compare the source
            if source1 != source2:
                # increment the error count
                self._e += 1

                # save the full page sources
                self.save_file("E%s-S1.txt" % self._e, self._a.driver.page_source.encode('utf-8'))
                self.save_file("E%s-S2.txt" % self._e, self._b.driver.page_source.encode('utf-8'))

                # save screenshots
                self._a.driver.save_screenshot("E%s-S1.png" % self._e)
                self._b.driver.save_screenshot("E%s-S2.png" % self._e)

                # do the diff and save to a file
                import difflib
                fromfile = self.get_context(self._a)
                tofile = self.get_context(self._b)
                result = list(difflib.unified_diff(source1.splitlines(1),source2.splitlines(1), fromfile=fromfile, tofile=tofile))
                self.save_file("E%s-D.txt" % self._e, result)

            print source1 == source2
            return self

        # check if this is a builtin type
        if a.__class__.__module__ == '__builtin__' and b.__class__.__module__ == '__builtin__':
            if a == b:
                return a
            else: return 0

        # need to return a wrapper object if not a Page or builtin
        return wrapper(a, b)

    def clean_source(self, source):
        import re
        source = re.sub(r'<([^/][a-zA-Z]*)\s?[^>]*>', r'<\1>', source)
        source = re.sub(r'<font>(G[^<]*)</font>',r'<font></font>', source)
        source = re.sub(r'<td>\xa9[^<]*</td>', r'<td></td>', source)
        source = re.sub(r'submitTime = [0-9]*;', r'', source)
        # @todo: handle project snapshot differences
        return source

    def save_file(self, file, s):
        f = open(file, "w")
        if type(s) is list:
            for line in s:
                f.write(line)
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


