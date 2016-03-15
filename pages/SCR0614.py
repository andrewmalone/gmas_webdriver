# POPUP!
from pages.Page import Page
from pages.elements import Radio


class SCR0614(Page):
    """
    SCR_0614 Opportunity lookup popup
    """
    locators = {
        "ok": "name=OpportunityValidationResultEvent",
        "competition": "css=[name=competitionRadio]"
    }

    competition = Radio("competition", "competition id selection")

    def ok(self):
        """
        Click <Ok>
        Closes the popup and returns to the main window
        """
        self.find("ok").click()
        self.driver.switch_to_window(self.driver.window_handles[0])

    @property
    def competition_count(self):
        """
        Number of competitions on the page
        """
        return len(self.finds("competition"))

    def select_competition(self, n):
        """
        Selects the nth competition
        """
        self.finds("competition")[n - 1].click()
