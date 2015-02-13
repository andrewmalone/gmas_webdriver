from pages.Page import Page


class SCR0398(Page):
    """
    SCR_0398 Confirm delete research team member
    """
    locators = {
        "yes": "ConfirmDeleteResearchPersonYesEvent"
    }

    def ok(self):
        """
        Click <Yes>
        Goes to SCR_0015
        """
        return self.go("yes")
