from pages.Page import Page


class SCR0509(Page):
    """
    SCR_0509 confirm required signatures
    """
    locators = {
        "next": "name=ConfirmRequiredSignaturesNextEvent"
    }

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0487
        """
        self.go("next")
