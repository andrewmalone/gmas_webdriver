from pages.Page import Page


class SCR0135(Page):
    """ SCR_0135 Document Detail """
    locators = {
        "unlock": "name=DocumentUnlockEvent",
        "download": "css=a[href*='DocumentActionViewEvent'] img",
        "delete": "name=DocumentActionDeleteEvent"
    }

    def unlock(self):
        """
        Click the <unlock> button
        """
        return self.go("unlock")

    def delete(self):
        """
        Click the <Delete> button
        Goes to SCR_0136
        """
        return self.go("delete")