class Element(object):
    def __init__(self, locator):
        self.locator = locator


class Text(Element):
    def __set__(self, obj, val):
        elem = obj.find(self.locator)
        elem.clear()
        elem.send_keys(val)

    def __get__(self, obj, type=None):
        elem = obj.find(self.locator)
        return elem.get_attribute("value")


class Select(Element):
    def __set__(self, obj, val):
        from selenium.webdriver.support.select import Select as WDSelect
        elem = WDSelect(obj.find(self.locator))
        elem.select_by_visible_text(val)

    def __get__(self, obj, type=None):
        from selenium.webdriver.support.select import Select as WDSelect
        elem = WDSelect(obj.find(self.locator))
        return elem.first_selected_option.text


class Radio(Element):
    def __set__(self, obj, val):
        if "[value='REPLACE']" not in obj.locators[self.locator]:
            obj.locators[self.locator] += "[value='REPLACE']"  # this is kind of a hack?
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
