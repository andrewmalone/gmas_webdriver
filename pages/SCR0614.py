# POPUP!
from pages.Page import Page


class SCR0614(Page):
    """
    SCR_0614 Opportunity lookup popup
    """
    locators = {
        "ok": "name=OpportunityValidationResultEvent"
    }

    def ok(self):
        """
        Click <Ok>
        Closes the popup and returns to the main window
        """
        self.find("ok").click()
        self.driver.switch_to_window(self.driver.window_handles[0])