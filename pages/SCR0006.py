from pages.Page import Page
from pages.elements import Text


class SCR0006(Page):
    locators = {
        "total_direct": "name=totalDirectCost",
        "total_indirect": "name=totalIndirectCost",
        "edit indirect": "name=EditProposedBudgetEditIndirectCostEvent",
        "editbox": "css=input[name$='__budgetEntryAmount']",
        "ok": "name=EditProposedBudgetOKEvent"
    }

    total_direct = Text("total_direct", "Total direct cost")
    total_indirect = Text("total_indirect", "Total indirect cost")

    def enter_first(self, str):
        elems = self.finds("editbox")
        for elem in elems:
            if elem.is_displayed() is True:
                elem.send_keys(str)
                break

    def edit_indirect(self):
        # to SCR_0018
        return self.go("edit indirect")

    def ok(self):
        return self.go("ok")
