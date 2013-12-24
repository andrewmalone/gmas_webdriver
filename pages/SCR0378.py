from pages.Page import Page
from pages.elements import Checkbox


class SCR0378(Page):
    """
    SCR_0378 Select accounts for at-risk
    Currently only supports checking the first account
    """
    locators = {
        "checkbox": "css=input[type=checkbox][name$=checkboxFlag]",
        "next": "SelectRequestedAtRiskAccountsNextEvent"
    }

    checkbox = Checkbox("checkbox", "Checkbox to select at-risk account")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0379
        """
        return self.go("next")