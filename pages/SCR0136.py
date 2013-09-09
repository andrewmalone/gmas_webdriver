from pages.Page import Page


class SCR0136(Page):
    """
    SCR_0136 Delete document confirmation
    """
    locators = {
        "yes": "name=DeleteDocumentYesEvent",
        "no": "name=DeleteDocumentNoEvent"
    }

    def ok(self):
        """
        Click <Yes>
        Goes to SCR_0433
        """
        return self.go("yes")

    def cancel(self):
        """
        Click <No>
        Goes to SCR_0433 or SCR_0135
        """
        return self.go("no")