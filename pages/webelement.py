"""
Implements a base wrapper class used by all page objects - mainly used to create convenience methods for locating page elements.
"""
from selenium.webdriver.common.by import By


class GMWebElement(object):
    """
    Base wrapper class for page objects.

    Implements methods to make writing locators easier. A locator can use the format "method=locator", and all location types
    can then use a common find method.

    For example, the following locators are equivalent:

    * "css=input[name=someElement]"
    * "name=someElement"
    * "xpath=//input[@name='someElement']"
    """
    def find(self, locator, replace=False):
        """
        Find and return a WebElement

        arguments:
        locator - string representing the key in the page's internal `locators` dictionary
        replace - optional string to replace the text "REPLACE" in the locator
        """
        locator = self.locator(locator, replace)
        return self.driver.find_element(*locator)

    def finds(self, locator, replace=False):
        """
        Find and return a list of WebElements

        arguments:
        locator - string representing the key in the page's internal `locators` dictionary
        replace - optional string to replace the text "REPLACE" in the locator
        """
        locator = self.locator(locator, replace)
        return self.driver.find_elements(*locator)

    def find_element(self, locator):
        """Find and return a WebElement using a locator string ("method=locator")"""
        locator = self.locator_from_string(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Find and return a list of WebElements using a locator string ("method=locator")"""
        locator = self.locator_from_string(locator)
        return self.driver.find_elements(*locator)

    def locator(self, locator, replace=False):
        """Retrieve a locator string from the internal locators dictionary"""
        locator = self.locators[locator]
        if replace:
            locator = locator.replace("REPLACE", str(replace))
        return self.locator_from_string(locator)

    def locator_from_string(self, locator):
        """Convert a locator string to a (By, locator) tuple"""
        locator_map = {
            "css": By.CSS_SELECTOR,
            "id": By.ID,
            "name": By.NAME,
            "link": By.LINK_TEXT,
            "partial": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH
        }
        if locator.find("=") == -1:
            locator_type = "name"
            locator_value = locator
        else:
            locator_type = locator[:locator.find("=")]
            locator_value = locator[locator.find("=") + 1:]
        if locator_type == "event":
            locator_type = "css"
            locator_value = "a[href*=%s]" % locator_value
        return (locator_map[locator_type], locator_value)
