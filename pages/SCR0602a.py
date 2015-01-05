from pages.Page import Page


class SCR0602a(Page):
    """
    SCR_0602a Disable subactivity confirmation
    """
    locators = {
        "ok": "ConfirmSubactivityDisableYesEvent"
    }

    def ok(self):
        """
        Click <Yes>
        Goes to SCR_0187
        """
        return self.go("ok")
