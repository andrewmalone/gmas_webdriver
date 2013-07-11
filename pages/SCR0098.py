from pages.Page import Page


class SCR0098(Page):
    locators = {
        "PI link": "link=Principal Investigator",
        "add member": "name=RequestAddResearchTeamMemberEvent",
        "next": "name=CreateResearchTeamNextEvent"
    }

    def add_member(self):
        self.find("add member").click()
        return self.load_page()

    def edit_pi(self):
        self.find("PI link").click()
        return self.load_page()

    def ok(self):
        self.find("next").click()
        return self.load_page()

