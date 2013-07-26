from pages.Page import Page

locators = {
    "add team member": "name=AddTeamMemberEvent",
    "PI link": "link=Principal Investigator"
}


class SCR0015(Page):
    """
    SCR_0015 Research team list
    {note}
    This has only been tested with the request version of the screen. Also, there's no great way to go to a person by name (will be added eventually)
    {note}
    """
    locators = locators

    def add_team_member(self):
        """
        Click <Add team member>
        Goes to SCR_0252
        """
        self.find_element(locators["add team member"]).click()
        from pages.SCR0252 import SCR0252
        return SCR0252(self.driver)

    def goto_pi(self):
        """
        Click the "Principal investigator" link
        Goes to SCR_0363
        """
        self.find("PI link").click()
        return self.load_page()

    def goto_member(self, num):
        """
        Click the research team link for the nth entry in the list (0 based)
        Goes to SCR_0363
        """
        # ResearchTeamMemberViewEvent
        elems = self.find_elements("css=a[href*='ResearchTeamMemberViewEvent']")
        elems[num].click()
        return self.load_page()