from pages.Page import Page


class SCR0098(Page):
    """
    SCR_0098 RGS research team list
    """
    locators = {
        "PI link": "link=Principal Investigator",
        "add member": "name=RequestAddResearchTeamMemberEvent",
        "next": "name=CreateResearchTeamNextEvent"
    }

    def add_member(self):
        """
        Click <Add team member>
        Goes to SCR_0365
        """
        self.find("add member").click()
        return self.load_page()

    def edit_pi(self):
        """
        Click the PI link
        Goes to SCR_0365
        """
        self.find("PI link").click()
        return self.load_page()

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0099
        """
        self.find("next").click()
        return self.load_page()

