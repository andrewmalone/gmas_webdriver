from pages.Page import Page


class SCR0006(Page):
    locators = {
        "editbox": "css=input[name$='__budgetEntryAmount']",
        "ok": "name=EditProposedBudgetOKEvent"
    }

    def enter_first(self, str):
        elems = self.finds("editbox")
        for elem in elems:
            if elem.is_displayed() is True:
                elem.send_keys(str)
                break

    def ok(self):
        return self.go("ok")
