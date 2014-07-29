from pages.Page import Page
from pages.elements import Text, Row, Select


class SCR0645(Page):
    """
    SCR_0645 Confirm research team
    """
    locators = {
        "ok": "name=ConfirmResearchTeamOkEvent",
        "person row": "css=#dataRow"
    }

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
            "commitment_flag": "css=select[name$=sponsorCommitmentFlag]"
        }

        cal_effort = Text("cal_effort", "Calendar effort")
        sponsor_commitment = Select("commitment_flag", "Sponsor commitment")
