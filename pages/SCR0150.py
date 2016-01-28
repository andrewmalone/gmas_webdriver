from pages.Page import Page


class SCR0150(Page):
    """
    SCR_0150 Edit receivable
    """
    locators = {
        "ok": "EditReceivableOkEvent"
    }

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0296 Receivable list
        """
        return self.go("ok")
