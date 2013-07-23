from pages.Page import Page


class SCR0102(Page):
    """
    SCR_0102 Budget Categories
    """
    locators = {
        "next": "name=BudgetCategoriesNextEvent"
    }

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0091, SCR_0228, or SCR_0098
        """
        self.find("next").click()
        return self.load_page()
