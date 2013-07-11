from pages.Page import Page

locators = {
    "add team member": "name=AddTeamMemberEvent",
    "PI link": "link=Principal Investigator"
}


class SCR0015(Page):
    locators = locators

    def add_team_member(self):
        self.find_element(locators["add team member"]).click()
        from pages.SCR0252 import SCR0252
        return SCR0252(self.driver)

    def goto_pi(self):
        self.find("PI link").click()
        return self.load_page()

    def goto_member(self, num):
        # ResearchTeamMemberViewEvent
        elems = self.find_elements("css=a[href*='ResearchTeamMemberViewEvent']")
        elems[num].click()
        return self.load_page()