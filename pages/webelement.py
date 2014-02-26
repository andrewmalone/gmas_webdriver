from selenium.webdriver.common.by import By

locator_map = {
    "css": By.CSS_SELECTOR,
    "id": By.ID,
    "name": By.NAME,
    "link": By.LINK_TEXT,
    "partial": By.PARTIAL_LINK_TEXT,
    "xpath": By.XPATH
}

class GMWebElement(object):
    def find(self, locator, replace=False):
        locator = self.locators[locator]
        if replace:
            locator = locator.replace("REPLACE", str(replace))
        return self.find_element(locator)

    def finds(self, locator, replace=False):
        locator = self.locators[locator]
        if replace:
            locator = locator.replace("REPLACE", str(replace))
        return self.find_elements(locator)

    def find_element(self, locator):
        if locator.find("=") == -1:
            locator_type = "name"
            locator_value = locator
        else:
            locator_type = locator[:locator.find("=")]
            locator_value = locator[locator.find("=") + 1:]
        if locator_type == "event":
            locator_type = "css"
            locator_value = "a[href*=%s]" % locator_value
        return self.driver.find_element(locator_map[locator_type], locator_value)

    def find_elements(self, locator):
        if locator.find("=") == -1:
            locator_type = "name"
            locator_value = locator
        else:
            locator_type = locator[:locator.find("=")]
            locator_value = locator[locator.find("=") + 1:]
        if locator_type == "event":
            locator_type = "css"
            locator_value = "a[href*=%s]" % locator_value
        return self.driver.find_elements(locator_map[locator_type], locator_value)