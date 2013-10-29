# TODO: factor out opportunity lookup
from pages.Page import Page
from pages.elements import Text

locators = {
    "opportunity": "name=opportunity_id",
    "validate": "css=img[alt='Validate']",
    "next": "name=EnterOpportunityNextEvent"
}


class Lookup_opportunity(object):
    """
    Performs an opportunity search (opens popup and presses <ok>)
    """
    def __set__(self, obj, val):
        obj._lookup_opportunity(val)

    def __get__(self, obj, type=None):
        pass


class SCR0613(Page):
    """
    SCR_0613 Opportunity search
    """
    locators = locators
    opportunity_text = Text("opportunity", "opportunity number text box")
    opportunity = Lookup_opportunity()

    def _lookup_opportunity(self, opportunity):
        self.opportunity_text = opportunity
        self.find("validate").click()
        self.switch_to_popup()
        from pages.SCR0614 import SCR0614
        popup = SCR0614(self.driver)
        popup.ok()
        return self

    def ok(self):
        """
        Clicks <Next>
        Goes to SCR_0231 or SCR_0231b
        """
        self.find("next").click()
        return self.load_page()
