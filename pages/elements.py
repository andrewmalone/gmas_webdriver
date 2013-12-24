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
            return self.element.is_displayed()

        def is_enabled(self):
            return self.element.is_enabled()

class Text(Element):
    """ (Text) """
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        elem.clear()
        elem.send_keys(val)
        # fire the onchange! 
        # TODO - figure out if there's a non-javascript webdriver native way to do this...
        # There's a bug on SCR_0617 that throws a javascript error in the onchange event.
        try:
            screen = obj.get_current_page()
        except AttributeError:
            screen = ""
        if "SCR0617" not in screen:
            script = """
                if (arguments[0].onchange) arguments[0].onchange();
                else if (arguments[0].onblur) arguments[0].onblur();
            """
            elem.parent.execute_script(script, elem)

    def __get__(self, obj, type=None):
        elem = obj.find(self.locator)
        r = self.returnObj(elem.get_attribute("value"))
        r.element = elem
        return r


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
        from selenium.webdriver.support.select import Select as WDSelect
        elem = WDSelect(obj.find(self.locator))
        r = self.returnObj(elem.first_selected_option.text)
        r.element = obj.find(self.locator)
        r.p = self
        return r
 

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
                return True
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
        pass


class File(Element):
    """ (File) """
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        elem.send_keys(val)

    def __get__(self, obj, cls=None):
        pass