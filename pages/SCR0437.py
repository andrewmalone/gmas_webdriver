from pages.Page import Page
from pages.elements import Text, Row


class SCR0437(Page):
    """
    SCR_0437 Edit modular budget
    """
    locators = {
        "budget_row": "xpath=//input[@type='text'][contains(@name, 'directAmount')]/../..",
        "ok": "EditNIHModularBudgetOKEvent",
        "edit_idc": "EditNIHModularBudgetEditIDCRateEvent"
    }

    @property
    def budget_rows(self):
        """
        Returns a list of budget rows on the page
        //Budget_row
        """
        return [self.Budget_row(row, self) for row in self.finds("budget_row")]

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0006 or ?
        """
        return self.go("ok")

    def edit_idc(self):
        """
        Click <Edit IDC rate>
        Goes to SCR_0020
        """
        return self.go("edit_idc")

    class Budget_row(Row):
        locators = {
            "direct": "css=input[type=text][name$=directAmount]",
            "subject_to_oh": "css=input[type=text][name$=subjectToOverheadAmount]",
            "subfa": "css=input[type=text][name$=consortiumAmount]"
        }

        direct = Text("direct", "Requested direct amount")
        subject_to_oh = Text("subject_to_oh", "Subject to IDC")
        sub_fa = Text("subfa", "Subagreement F&A")

        def fill(self, amounts=(0, 0, 0)):
            """
            Fill the row with values - takes a tuple with three values
            """
            self.direct = amounts[0]
            self.subject_to_oh = amounts[1]
            self.sub_fa = amounts[2]
