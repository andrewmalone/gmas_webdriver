from pages.Page import Page
from pages.elements import Select, Radio, Text


class SCR0365(Page):
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

    role = Select("role")
    human_subjects = Radio("hs")
    key = Radio("key")
    person_text = Text("person input")
    investigator = Radio("investigator")

    def lookup_person(self, person):
        self.person_text = person
        self.find("person lookup").click()
        self.w.until(lambda e: self.find("person lookup match"))
        return self

    def ok(self):
        self.find("ok").click()
        return self.load_page()
