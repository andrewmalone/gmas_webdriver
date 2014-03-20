from pages.Page import Page


class SCR0050(Page):
    """
    SCR_0050 Standing Team
    """
    locators = {
        "add member": "css=a[href*=AddStandingTeamMemberEvent] img",
        "link": "css=a[href*=ViewPersonAssignmentEvent]",
        "link id": "css=a[href*='teamMemberPersonId=REPLACE']",
        "link name": "link=REPLACE",
        "assignments": "event=ViewTeamMemberAssignmentsEvent",
        "roles": "event=ViewTeamRolesEvent",
        "scope": "event=ViewTeamOrgCoverageEvent"
    }

    @property
    def member_count(self):
        """
        Count of people on the team
        """
        return len(self.finds("link"))

    def add_member(self):
        """
        Click <Add team member>
        Goes to SCR_0051
        """
        return self.go("add member")

    def goto_member(self, name=None, id=None, num=None):
        """
        Clicks a team member's name
        Name (exact match), person id, or row number must be specified
        Goes to SCR_0055

        Examples:
        * **name**: `p.goto_member(name="Malone, Andrew")`
        * **id**: `p.goto_member(id=5000018)`
        * **row**: `p.goto_member(num=2)` (clicks the second link)
        """
        if name is not None:
            return self.go("link name", name)
        if id is not None:
            return self.go("link id", id)
        if num is not None:
            link = self.finds("link")[num - 1]
            link.click()
            return self.load_page()

    def goto_member_num(self, num):
        """
        (not sure if this will stay here)
        """
        return self.goto_member(num=num)

    def goto_assignments(self):
        """
        Click the <View team assignments> button
        Goes to SCR_0366
        """
        return self.go("assignments")

    def goto_roles(self):
        """
        Click the <Team roles> button
        Goes to SCR_0539
        """
        return self.go("roles")

    def goto_orgs(self):
        """
        Click the <Team org coverage> button
        Goes to SCR_0540
        """
        return self.go("scope")

