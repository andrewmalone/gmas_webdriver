from pages.Page import Page, GMWebElement
from pages.elements import Text

class PersonRow(GMWebElement):
    locators = {
        "cal_effort": "css=#calculatedEffortId"
    }

    cal_effort = Text("cal_effort")

    def __init__(self, row, page):
        self.driver = page.driver
        

class SCR0645(Page):
    locators = {
        "ok": "name=ConfirmResearchTeamOkEvent",
        "person row": "css=#dataRow"
    }

    def ok(self):
        # to segment home
        return self.go("ok")

    def person(self, number):
        return PersonRow(self.finds("person row")[number - 1], self)

    def count_people(self):
        return len(self.finds("person row"))