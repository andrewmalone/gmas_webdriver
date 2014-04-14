from pages.Page import Page


class SCR0409(Page):
    """
    SCR_0409 Revise to resubmit confirmation
    """
    locators = {
        "ok": "ReviseRequestConfirmationYesEvent"
    }

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0402b
        """
        return self.go("ok")
