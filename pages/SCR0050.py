from pages.Page import Page


class SCR0050(Page):
    """
    SCR_0050 Standing Team
    """
    locators = {
        "add member": "css=a[href*=AddStandingTeamMemberEvent] img",
        "link": "css=a[href*=ViewPersonAssignmentEvent]",
        "link id": "css=a[href*='teamMemberPersonId=REPLACE']",
        "link name": "link=REPLACE"
    }

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

