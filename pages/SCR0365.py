from pages.Page import Page
from pages.elements import Select, Radio, Text, Checkbox
from pages.lookups import Lookup_person


class SCR0365(Page):
    """
    SCR_0365 Edit person in RGS
    """
    locators = {
        "hs": "css=input[name='isHumanSubjectInvolved']",
        "role": "name=roleId",
        "other role description": "name=otherRoleDescription",
        "person input": "name=personName",
        "key": "css=[name='KeyPersonnel']",
        "investigator": "css=[name='phsInvestigationFlag']",
        "tbd": "toBeDeterminedChecked",
        "ok": "name=ResearchTeamMemberOKEvent",
        "credential": "name=contactPersonCredential"
    }

    role = Select("role", "Role dropdown")
    other_role_description = Text("other role description", "Text box for other role description")
    human_subjects = Radio("hs", "Human subjects radio button (true/false)")
    key = Radio("key", "Key person radio button (true/false)")
    person_text = Text("person input", "Text box for person name/HUID")
    person = Lookup_person(person_text, "researchTeamMemberImage", "Research team member lookup")
    investigator = Radio("investigator", "Investigator radio button (true/false)")
    tbd = Checkbox("tbd", "TBD Checkbox")
    credential = Select("credential", "Credential for S2S submission")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0098
        """
        return self.go("ok")
