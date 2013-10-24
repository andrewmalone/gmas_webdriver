from pages.Page import Page


class SCR0091(Page):
    """
    SCR_0091 Subagreement list in RGS
    """
    locators = {
        "add": "name=RequestSubagreementsAddEvent",
        "ok": "name=RequestSubagreementsNextEvent"
    }

    def add_sub(self):
        """
        Click <Add subagreement>
        Goes to SCR_0092
        """
        return self.go("add")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0228 or SCR_0098
        """
        return self.go("ok")