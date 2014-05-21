from pages.Page import Page
from pages.elements import Text


class SCR0512(Page):
    """
    SCR_0512 Confirm continuation period dates
    """
    locators = {
        "next": "name=ContinuationPeriodConfirmationNextEvent",
        "start": "proposedStartDate",
        "end": "proposedEndDate"
    }

    start = Text("start", "Proposed start date")
    end = Text("end", "Proposed end date")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0231
        """
        return self.go("next")
