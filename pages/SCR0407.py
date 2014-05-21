from pages.Page import Page


class SCR0407(Page):
    """
    SCR_0407 Delete request confirmation
    """
    locators = {
        "ok": "DeleteRequestConfirmationYesEvent"
    }

    def ok(self):
        """
        Click <Yes>
        Goes to Segment Home SCR_0104b (maybe others)
        """
        return self.go("ok")
