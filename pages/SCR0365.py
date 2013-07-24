from pages.Page import Page
from pages.elements import Select, Radio, Text


class SCR0365(Page):
    """
    SCR_0365 Edit person in RGS
    """
    locators = {
        "hs": "css=input[name='isHumanSubjectInvolved']",
        "role": "name=roleId",
        "person input": "name=personName",
        "person lookup": "css=a[href*='researchTeamMemberImage'] img",
        "person lookup match": "css=img[name='researchTeamMemberImage'][src*='i_match.gif']",
        "key": "css=[name='KeyPersonnel']",
        "investigator": "css=[name='phsInvestigationFlag']",
        "ok": "name=ResearchTeamMemberOKEvent"
    }

    role = Select("role", "Role dropdown")
    human_subjects = Radio("hs", "Human subjects radio button (true/false)")
    key = Radio("key", "Key person radio button (true/false)")
    person_text = Text("person input", "Text box for person name/HUID")
    investigator = Radio("investigator", "Investigator radio button (true/false)")

    def lookup_person(self, huid):
        """
        Enters and HUID and does the person lookup (will only work with HUID)
        """
        self.person_text = huid
        self.find("person lookup").click()
        self.w.until(lambda e: self.find("person lookup match"))
        return self

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0098
        """
        self.find("ok").click()
        return self.load_page()
