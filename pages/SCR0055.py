from pages.Page import Page


class SCR0055(Page):
    """
    SCR_0055 Person team assignments
    """
    locators = {
        "remove": "css=a[href*=PersonAssignmentManagerRemoveTeamMemberEvent] img"
    }

    def remove_member(self):
        """
        Click <Remove member>
        Goes to SCR_0050
        """
        return self.go("remove")