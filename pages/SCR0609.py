from pages.Page import Page


class SCR0609(Page):
    locators = {

    }

    def set_form(self, form_name, value):
        locator = "css=input[name$=__eFormName][value='%s']" % form_name
        name = self.find(locator).get_attribute("name").replace("__eFormName", "__optionalFlag")
        locator = "css=input[name='%s'][value='%s]" % (name, value)
        self.find(locator).click()
