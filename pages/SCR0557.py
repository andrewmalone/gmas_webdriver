from pages.Page import Page
from pages.elements import Select


class SCR0557(Page):
    """
    SCR_0557 Account research locations
    """
    locators = {
        "ok": "AccountResearchLocationOkEvent",
        "location": "css=select[name$=researchLocationId]"
    }

    location = Select("location", "Research location")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0474
        """
        return self.go("ok")
