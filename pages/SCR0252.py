from pages.Page import Page
from pages.elements import Select, Text, Radio, Row, Checkbox
from pages.lookups import Lookup_person

appt_mapping = {
    "_method": "value",
    "12": "9101",
    "9": "9102",
    "3": "9103"
}


class SCR0252(Page):
    """
    SCR_0252
    Edit research team member
    """
    locators = {
        "role": "name=role",
        "appt": "name=appointment",
        "name input": "name=personName",
        "human subjects": "css=[name='isMemberInvolvedWithHumanSubjects'][value='REPLACE']",
        "PHS": "css=[name='isMemberPHSInvestigator'][value='REPLACE']",
        "ok": "name=EditResearchPersonnelOkEvent",
        "budget row": "xpath=//input[contains(@name,'__effort')]/../.."
    }

    role = Select("role", "Role")
    appt = Select("appt", "Appointment", mapping=appt_mapping)
    name_text = Text("name input", "Text entry field for person name")
    name = Lookup_person(name_text, 'personLookupImage', "Research team person lookup")
    human_subjects = Radio("human subjects", "Human subjects radio button")
    phs = Radio("PHS", "PHS investigator radio button")

    def _to_list(self, val):
        l = []
        if type(val) is list:
            l = val
        else:
            l = [val for i in range(len(self.finds("budget row")))]

        return l

    # TODO: make this cleaner (make into a descriptor?)
    def set_effort(self, val):
        """
        Shorcut method - set all effort boxes to the same value
        """
        val = self._to_list(val)
        for i in range(len(self.finds("budget row"))):
            self.budget(i + 1).effort = val[i]

    def set_salary(self, val):
        """
        Shorcut method - set all salary boxes to the same value
        """
        val = self._to_list(val)
        for i in range(len(self.finds("budget row"))):
            self.budget(i + 1).salary = val[i]

    def set_fringe(self, val):
        """
        Shorcut method - set all fringe boxes to the same value
        """
        val = self._to_list(val)
        for i in range(len(self.finds("budget row"))):
            self.budget(i + 1).fringe = val[i]

    def set_key(self, val):
        """
        Shorcut method - set all key checkboxes to the same value
        """
        val = self._to_list(val)
        for i in range(len(self.finds("budget row"))):
            self.budget(i + 1).key = val[i]

    @property
    def budgets(self):
        """
        Returns a list of budget rows
        """
        rows = []
        for row in self.finds("budget row"):
            rows.append(self.Budget_row(row, self))

        return rows

    @property
    def budget_count(self):
        """
        Number of budget rows
        """
        return len(self.finds("budget row"))

    def budget(self, n):
        """
        Returns the nth budget period row (1 indexed)
        //Budget_row
        """
        row = self.finds("budget row")[n - 1]
        return self.Budget_row(row, self)

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0363 or SCR_0006
        """
        return self.go("ok")

    class Budget_row(Row):
        locators = {
            "effort": "css=input[name$='__effort']",
            "key": "css=input[name$='__keyPersonFlag']",
            "salary": "css=input[name$='__requestedSalary']",
            "fringe": "css=input[name$='__fringeAmount']"
        }

        effort = Text("effort", "%% Effort")
        salary = Text("salary", "Salary")
        fringe = Text("fringe", "Fringe")
        key = Checkbox("key", "Key person checkbox")
