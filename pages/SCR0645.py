from pages.Page import Page
from pages.elements import Text, Row, Select
from pages.lookups import Lookup_person


class SCR0645(Page):
    """
    SCR_0645 Confirm research team
    """
    locators = {
        "ok": "name=ConfirmResearchTeamOkEvent",
        "person row": "css=tr#dataRow:not([style*='display: none'])",
        "add person": "personName"
    }

    person_text = Text("add person", "Text box to add a person")
    new_person = Lookup_person(person_text, "personLookupImage", "Add person lookup")

    def ok(self):
        """
        Click <Ok>
        goes to SCR_0104b
        """
        # to segment home
        return self.go("ok")

    def person(self, number):
        """
        Returns a row for an individual research team member
        //PersonRow
        """
        return self.PersonRow(self.finds("person row")[number - 1], self)

    @property
    def person_count(self):
        """
        Returns the number of people on the screen
        """
        return len(self.finds("person row"))

    class PersonRow(Row):
        locators = {
            "cal_effort": "css=#calculatedEffortId",
            "commitment_flag": "css=select[name$=sponsorCommitmentFlag]",
            "role": "css=select[name$=role]",
            "key": "css=select[name$=isKeyPerson]",
            "investigator": "css=select[name$=isMemberPHSInvestigator]",
            "human subjects": "css=select[name$=isMemberInvolvedWithHumanSubjects]",
            "delete": "id=delIcon"
        }

        cal_effort = Text("cal_effort", "Calendar effort")
        sponsor_commitment = Select("commitment_flag", "Sponsor commitment")
        role = Select("role", "Research team role")
        key = Select("key", "Key person flag")
        investigator = Select("investigator", "PHS investigator flag")
        human_subjects = Select("human subjects", "Human Subjects flag")

        def delete(self):
            """
            Click the delete icon for the row
            """
            self.find("delete").click()
