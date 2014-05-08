from pages.Page import Page


class SCR0450(Page):
    """
    SCR_0450 Sub under development
    """
    locators = {
        "budget": "event=ViewSubagreementDetailBudgetEvent"
    }

    def goto_budget(self):
        """
        Clicks the <Subagreement detailed budget> button
        Goes to SCR_0428
        """
        return self.go("budget")
