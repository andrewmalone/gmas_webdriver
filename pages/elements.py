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
            if self.element.tag_name == "select":
                if self.p.mapping is not None:
                    options = [option for option in self.p.mapping.keys() if option != "_method"]
                    return options
                from selenium.webdriver.support.select import Select as WDSelect
                e = WDSelect(self.element)
                options = []
                for option in e.options:
                    if option.get_attribute("value") != "":
                        options.append(option.text)
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
            return False


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
            r.p = self
            return r
        except (NoSuchElementException, UnexpectedTagNameException):
            return False
 

class Radio(Element):
    """ (Radio button) """
    def __set__(self, obj, val):
        if "[value='REPLACE']" not in obj.locators[self.locator]:
            obj.locators[self.locator] += "[value='REPLACE']"  # this is kind of a hack?
        if self.mapping != None:
            val = self.mapping[val]
        elem = obj.find(self.locator, val)
        elem.click()

    def __get__(self, obj, cls=None):
        """
        Get the value of a radio button (currently selected)
        returns False if the element is not on the page or isn't displayed
        """
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
                return r
            return False


class Radio_refresh(Radio):
    def __set__(self, obj, val):
        super(Radio_refresh, self).__set__(obj, val)
        return obj


class Checkbox(Element):
    """ (Checkbox) """
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        if val == True:
            if elem.get_attribute("checked") != "true":
                elem.click()
        if val == False:
            if elem.get_attribute("checked") == "true":
                elem.click()

    def __get__(self, obj, cls=None):
        try:
            elem = obj.find(self.locator)
        except:
            # TODO: figure out what to return here - also, think about refactoring everything in the same way
            return self.returnObj(None)
        attr = elem.get_attribute("checked")
        if attr == None:
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
    def __init__(self, row, page):
        self.driver = row
        self.page = page

    def _go(self, locator):
        self.find(locator).click()
        return self.page.load_page()


class RText(Element):
    """ (readonly text) """
    def __set__(self, obj, val):
        pass

    def __get__(self, obj, cls=None):
        elem = obj.find(self.locator)
        return elem.text