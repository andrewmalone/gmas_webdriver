from pages.Page import Page
from pages.elements import Select, Radio, Text
from pages.lookups import Lookup_person


class SCR0365(Page):
    """
    SCR_0365 Edit person in RGS
    """
    locators = {
        "hs": "css=input[name='isHumanSubjectInvolved']",
        "role": "name=roleId",
        "person input": "name=personName",
        "key": "css=[name='KeyPersonnel']",
        "investigator": "css=[name='phsInvestigationFlag']",
        "ok": "name=ResearchTeamMemberOKEvent"
    }

    role = Select("role", "Role dropdown")
    human_subjects = Radio("hs", "Human subjects radio button (true/false)")
    key = Radio("key", "Key person radio button (true/false)")
    person_text = Text("person input", "Text box for person name/HUID")
    person = Lookup_person(person_text, "researchTeamMemberImage", "Research team member lookup")
    investigator = Radio("investigator", "Investigator radio button (true/false)")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0098
        """
        return self.go("ok")
