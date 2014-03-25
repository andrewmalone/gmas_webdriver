from pages.Page import Page
import utilities.xpath as xpath


class SCR0015(Page):
    """
    SCR_0015 Research team list

    This has only been tested with the request version of the screen. Also, there's no great way to go to a person by name (will be added eventually)
    """
    locators = {
        "add team member": "name=AddTeamMemberEvent",
        "PI link": "link=Principal Investigator",
        "edit team": "name=EditResearchTeamButton",
        "person row": xpath.parent_row_of_event("ResearchPersonNameLinkEvent"),
        "person links": "event=ResearchPersonNameLinkEvent",
        "role links": "event=ResearchTeamMemberViewEvent"
    }

    @property
    def people_count(self):
        """
        Number of people showing in the list
        """
        return len(self.finds("role links"))

    def add_team_member(self):
        """
        Click <Add team member>
        Goes to SCR_0252
        """
        return self.go("add team member")

    def goto_pi(self):
        """
        Click the "Principal investigator" link
        Goes to SCR_0363
        """
        return self.go("PI link")

    def goto_name(self, num):
        """
        Click the nth name on the screen
        Goes to SCR_0025
        """
        self.finds("person links")[num - 1].click()
        return self.load_page()

    def goto_role(self, num):
        """
        Click the nth role on the screen
        Goes to SCR_0363
        """
        self.finds("role links")[num - 1].click()
        return self.load_page()

    def edit_team(self):
        """
        Click the <Edit research team button>
        Goes to SCR_0649
        """
        return self.go("edit team")