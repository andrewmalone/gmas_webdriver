from pages.Page import Page


class SCR0098(Page):
    """
    SCR_0098 RGS research team list
    """
    locators = {
        "PI link": "link=Principal Investigator",
        "add member": "name=RequestAddResearchTeamMemberEvent",
        "next": "name=CreateResearchTeamNextEvent",
        "mentor link": "link=Mentor",
        "cancel": "ResearchStaffCancelEvent",
        "save": "ResearchStaffSaveContinueLaterEvent"
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

    def edit_mentor(self):
        """
        Click the Mentor link
        Goes to SCR_0365
        """
        return self.go("mentor link")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0099
        """
        self.find("next").click()
        return self.load_page()

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
