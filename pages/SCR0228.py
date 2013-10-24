from pages.Page import Page


class SCR0228(Page):
    """
    SCR_0228 IFI list in RGS
    """
    locators = {
        "ok": "name=MultiTubOrgListNextEvent",
        "add": "name=MultiTubOrgListAddEvent"
    }

    def add_ifi(self):
        """
        Click <Add Tub/Org>
        Goes to SCR_0094
        """
        return self.go("add")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0098
        """
        return self.go("ok")