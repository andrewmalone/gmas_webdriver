from pages.Page import Page
from pages.elements import Text


class SCR0006(Page):
    """
    SCR_0006 Edit initial/competing budget
    """
    locators = {
        "total_direct": "name=totalDirectCost",
        "total_indirect": "name=totalIndirectCost",
        "edit indirect": "name=EditProposedBudgetEditIndirectCostEvent",
        "editbox": "css=input[name$='__budgetEntryAmount']",
        "next period": "css=input[title='Next period']",
        "ok": "name=EditProposedBudgetOKEvent"
    }

    total_direct = Text("total_direct", "Total direct cost")
    total_indirect = Text("total_indirect", "Total indirect cost")

    def enter_first(self, amount):
        """
        Enters a budget amount in the first available edit box
        (only works with category/line item budgets)
        """
        elems = self.finds("editbox")
        for elem in elems:
            if elem.is_displayed() is True:
                elem.send_keys(amount)
                break

    def next(self):
        """
        Click the next period arrow
        """
        return self.go("next period")

    def edit_indirect(self):
        """
        Click <Edit indirect costs>
        Goes to SCR_0018
        """
        return self.go("edit indirect")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0031 or SCR_0104b
        """
        return self.go("ok")
