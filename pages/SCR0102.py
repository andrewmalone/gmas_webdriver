from pages.Page import Page
from pages.elements import Radio


template_map = {
    "army": "9109",
    "energy": "9105",
    "ggov": "9113",
    "standard": "9110",
    "nasa": "9107",
    "nih": "9101",
    "nsf": "9104"
}


class SCR0102(Page):
    """
    SCR_0102 Budget Categories
    """
    locators = {
        "next": "name=BudgetCategoriesNextEvent",
        "template": "css=input[name=sponsorBudgetTemplate]",
        "save": "BudgetCategoriesSaveContinueLaterEvent",
        "cancel": "BudgetCategoriesCancelEvent"
    }

    template = Radio("template", "Budget template", mapping=template_map)

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0091, SCR_0228, or SCR_0098
        """
        return self.go("next")

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")

    def save(self):
        """
        Clicks <Save and continue later>
        Goes to SCR_0270 (for initial)
        """
        return self.go("save")
