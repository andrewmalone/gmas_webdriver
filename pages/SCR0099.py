from pages.Page import Page


class SCR0099(Page):
    """
    SCR_0099 Request admin team (RGS)
    """
    locators = {
        "next": "name=GrantsMgmtStaffNextEvent",
        "add": "name=GrantsMgmtStaffAddTeamMemberEvent",
        "cancel": "GrantsMgmtStaffCancelEvent",
        "save": "GrantsMgmtStaffSaveContinueLaterEvent"
    }

    def add_member(self):
        """
        Click <Add team member>
        Goes to SCR_0230
        """
        return self.go("add")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0097
        """
        return self.go("next")

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")

    def save(self):
        """
        Clicks <Save and continue later>
        Goes to SCR_0270 (for initial)
        """
        return self.go("save")
