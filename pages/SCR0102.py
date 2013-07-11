from pages.Page import Page


class SCR0102(Page):
    locators = {
        "next": "name=BudgetCategoriesNextEvent"
    }

    def ok(self):
        self.find("next").click()
        return self.load_page()
