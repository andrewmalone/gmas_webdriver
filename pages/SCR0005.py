from pages.Page import Page


class SCR0005(Page):
    """
    SCR_0005 RGS Cancel confirmation
    """
    locators = {
        "ok": "ConfirmRequestCancellationYesEvent"
    }

    def ok(self):
        """
        Click <Yes>
        Goes to SCR_0270 (for Initial)
        """
        return self.go("ok")
