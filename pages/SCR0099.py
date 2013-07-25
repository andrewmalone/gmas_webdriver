from pages.Page import Page


class SCR0099(Page):
    """
    SCR_0099 Request admin team (RGS)
    """
    locators = {
        "next": "name=GrantsMgmtStaffNextEvent",
        "add": "name=GrantsMgmtStaffAddTeamMemberEvent"
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
