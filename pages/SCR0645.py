from pages.Page import Page
from pages.elements import Text, Row
        

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

    def count_people(self):
        """
        Returns the number of people on the screen
        """
        return len(self.finds("person row"))

    class PersonRow(Row):
        locators = {
            "cal_effort": "css=#calculatedEffortId"
        }

        cal_effort = Text("cal_effort", "Calendar effort")