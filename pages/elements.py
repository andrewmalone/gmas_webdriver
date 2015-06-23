from pages.webelement import GMWebElement

#TODO - refactor to move return objects to more common methods
class Element(object):
    def __init__(self, locator, doc=None, mapping=None, docextra=None):
        self.locator = locator
        if doc != None:
            self.__doc__ = "%s%s" % (doc, self.__doc__)
        self.mapping = mapping
        # Add mapping info to docstring
        if mapping != None:
            self.__doc__ += "\nMapping:\n"
            for mapper in mapping:
                self.__doc__ += "* %s => %s\n" % (mapper, mapping[mapper])
        if docextra != None:
            self.__doc__ += docextra

    class returnObj(str):
        @property
        def element_type(self):
            tag_name = self.element.tag_name
            if tag_name == "select":
                return "select"
            elif tag_name == "input":
                return self.element.get_attribute("type")

        def is_displayed(self):
            if hasattr(self, "element"):
                return self.element.is_displayed()
            return False

        def is_enabled(self):
            return self.element.is_enabled()

        def set_random(self):
            if self.element.tag_name == "select":
                from selenium.webdriver.support.select import Select as WDSelect
                import random
                e = WDSelect(self.element)
                options = []
                for option in e.options:
                    if option.get_attribute("value") != "":
                        options.append(option.text)
                e.select_by_visible_text(random.choice(options))

        @property
        def options(self):
            options = []
            if self.element_type == "select":
                if self.parent.mapping is not None:
                    options = [option for option in self.parent.mapping.keys() if option != "_method"]
                    return options
                from selenium.webdriver.support.select import Select as WDSelect
                e = WDSelect(self.element)
                for option in e.options:
                    if option.get_attribute("value") != "":
                        options.append(option.text)
                return options
            if self.element_type == "radio":
                if self.parent.mapping is not None:
                    options = [option for option in self.parent.mapping.keys() if option != "_method"]
                    return options
                for element in self.elements:
                    options.append(element.get_attribute("value"))
                return options
            return ""


class Text(Element):
    """ (Text) """
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        elem.clear()
        elem.send_keys(val)
        # fire the onchange! 
        # TODO - figure out if there's a non-javascript webdriver native way to do this...
        script = """
            if (arguments[0].onchange) arguments[0].onchange();
            if (arguments[0].onblur) arguments[0].onblur();
            document.activeElement.blur();
        """
        from selenium.common.exceptions import WebDriverException
        try:
            elem.parent.execute_script(script, elem)
        except WebDriverException:
            pass

    def __get__(self, obj, type=None):
        from selenium.common.exceptions import NoSuchElementException
        try:
            elem = obj.find(self.locator)
            r = self.returnObj(elem.get_attribute("value"))
            r.element = elem
            return r
        except NoSuchElementException:
            return None


class Select(Element):
    """ (Select dropdown) """
    def __set__(self, obj, val):
        from selenium.webdriver.support.select import Select as WDSelect
        method = "text"
        elem = WDSelect(obj.find(self.locator))
        if self.mapping != None:
            val = self.mapping[val]
            if "_method" in self.mapping:
                method = self.mapping["_method"]
        if method == "text":
            elem.select_by_visible_text(val)
        elif method == "value":
            elem.select_by_value(val)

    def __get__(self, obj, type=None):
        from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException
        from selenium.webdriver.support.select import Select as WDSelect
        try:
            elem = WDSelect(obj.find(self.locator))
            r = self.returnObj(elem.first_selected_option.text)
            r.element = obj.find(self.locator)
            r.parent = self
            return r
        except (NoSuchElementException, UnexpectedTagNameException):
            return False
 

class Radio(Element):
    """ (Radio button) """
    def __set__(self, obj, val):
        if obj.mode == "old":
            if "[value='REPLACE']" not in obj.locators[self.locator]:
                obj.locators[self.locator] += "[value='REPLACE']"  # this is kind of a hack?
            if self.mapping is not None:
                val = self.mapping[val]
            elem = obj.find(self.locator, val)
            elem.click()
        if obj.mode == "convert":
            l = obj.locators[self.locator]
            if self.mapping is not None:
                val = self.mapping[val]
            val = "".join([s.capitalize() if i > 0 else s for i, s in enumerate(val.split("-"))])
            elem = obj.find_element("css=[id$={name}Panel] [id$={val}]".format(name=l, val=val))
            elem.click()

    def __get__(self, obj, cls=None):
        """
        Get the value of a radio button (currently selected)
        returns False if the element is not on the page or isn't displayed
        """
        if obj.mode == "old":
            l = obj.locators[self.locator]
            l = l.replace("[value='REPLACE']", "")
            # switch to try/catch
            from selenium.common.exceptions import NoSuchElementException
            try:
                el = obj.find_element(l)
            except NoSuchElementException:
                return False
            else:
                if el.is_displayed():
                    elements = obj.find_elements(l)
                    value = ""
                    for e in elements:
                        if e.get_attribute("checked") == "true":
                            value = e.get_attribute("value")
                    r = self.returnObj(value)
                    r.element = el
                    r.elements = elements
                    r.parent = self
                    return r
                return False
        if obj.mode == "convert":
            l = obj.locators[self.locator]
            # print l
            elements = obj.find_elements("css=input[type=radio][name$={}]:not(:disabled)".format(l))
            # print len(elements)
            if len(elements) == 0:
                return None
            for e in elements:
                # print e.get_attribute("value"), e.get_attribute("checked"), e.get_attribute("disabled")
                if e.get_attribute("checked") == "true":
                    value = e.get_attribute("value")
            r = self.returnObj(value)
            r.element = elements[0]
            r.elements = elements
            r.parent = self
            return r


class Radio_refresh(Radio):
    def __set__(self, obj, val):
        super(Radio_refresh, self).__set__(obj, val)
        return obj


class Checkbox(Element):
    """ (Checkbox) """
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        if val is True or val == "true":
            if elem.get_attribute("checked") != "true":
                elem.click()
        if val is False or val == "false":
            if elem.get_attribute("checked") == "true":
                elem.click()

    def __get__(self, obj, cls=None):
        try:
            elem = obj.find(self.locator)
        except:
            # TODO: figure out what to return here - also, think about refactoring everything in the same way
            return self.returnObj(None)
        attr = elem.get_attribute("checked")
        if attr is None:
            attr = "false"
        r = self.returnObj(attr)
        r.element = elem
        return r


class File(Element):
    """ (File) """
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        elem.send_keys(val)

    def __get__(self, obj, cls=None):
        pass


class Row(GMWebElement):
    """
    Base class for table rows
    """
    def __init__(self, row, page):
        """
        Initialize with an existing <tr> webelement and the parent page object
        """
        self.driver = row
        self.page = page
        if page.mode == "convert" and hasattr(self, "_locators"):
            self.locators = self._locators

    def _go(self, locator):
        """
        Click a locator and return the resulting page
        """
        self.find(locator).click()
        return self.page.load_page()

    def cell_text(self, n):
        """
        Returns the text from the nth td element of the row
        """
        cell = self.find_element("css=td:nth-child(%s)" % n)
        return cell.text

    @classmethod
    def cell(self, n):
        """
        Returns a css locator for the nth cell of the row
        """
        return "css=td:nth-child({})".format(n)


class RText(Element):
    """ (readonly text) """
    def __set__(self, obj, val):
        pass

    def __get__(self, obj, cls=None):
        from selenium.common.exceptions import NoSuchElementException
        try:
            elem = obj.find(self.locator)
        except NoSuchElementException:
            return None
        return elem.text
