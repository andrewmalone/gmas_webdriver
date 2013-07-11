from pages.Page import Page
from pages.elements import Text

locators = {
    "opportunity": "name=opportunity_id",
    "validate": "css=img[alt='Validate']",
    "next": "name=EnterOpportunityNextEvent"
}


class Lookup_opportunity(object):
    def __set__(self, obj, val):
        obj.lookup_opportunity(val)


class SCR0613(Page):
    locators = locators
    opportunity_text = Text("opportunity")
    opportunity = Lookup_opportunity()

    def lookup_opportunity(self, opportunity):
        self.opportunity_text = opportunity
        self.find("validate").click()
        self.switch_to_popup()
        from pages.SCR0614 import SCR0614
        popup = SCR0614(self.driver)
        popup.ok()
        return self

    def ok(self):
        self.find("next").click()
        return self.load_page()
