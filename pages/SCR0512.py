from pages.Page import Page


class SCR0512(Page):
    """
    SCR_0512 Confirm continuation period dates
    """
    locators = {
        "next": "name=ContinuationPeriodConfirmationNextEvent"
    }

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0231
        """
        return self.go("next")