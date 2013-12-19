from pages.Page import Page


class SCR0549(Page):
    locators = {
        "next": "name=RecordCommittedCostShareNextEvent"
    }

    def next(self):
        return self.go("next")