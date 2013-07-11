# POPUP screen!
from pages.Page import Page

locators = {
    "organization": "name=organizationSearchString",
    "organization type": "sizzle=select[name='organizationTypeString'] option:contains('REPLACE')",
    "search": "name=OrganizationLookupxEvent",
    "first result": "name=concatenatedOrganization",
    "ok": "sizzle=a:has(img[name='OrganizationSearchOkEvent'])"
}


class SCR0536x(Page):
    def set_name(self, name):
        e = self.find_element(locators["organization"])
        e.clear()
        e.send_keys(name)

    def select_type(self, type):
        # This is a hack...
        #helpers.ss(self.driver,"x")
        #self.w.until(lambda d: d.find_element_by_css_selector("select[name='organizationTypeString']"))
        #helpers.ss(self.driver,"y")
        self.find_element(locators["organization type"].replace("REPLACE", type)).click()

    def search(self):
        from selenium.common.exceptions import WebDriverException
        try:
            self.find_element(locators["search"]).click()
        except WebDriverException:
            # Getting some errors in Ghostdriver - trying to work around them
            self.find_element(locators["search"]).click()
        return self
        #return SCR0536x(self.driver)

    def select_first_result(self):
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.find_element(locators["first result"]).click()
        except NoSuchElementException:
            print "error!"
            self.find_element(locators["first result"]).click()

    def ok(self):
        #self.find_element(locators["ok"]).click()
        self.driver.execute_script("objectSelected()")
        # return to the main window
        self.driver.switch_to_window(self.driver.window_handles[0])
        # how do I know where I came from, and where I'm going back to? (maybe it doesn't matter)
