from pages.Page import Page


class SCR0332(Page):
    """
    SCR_0332 Finish request guided steps
    """
    locators = {
        "go request": "name=FinishGoToRequestEvent",
        "go budget": "name=FinishGoToBudgetEditBudgetEvent"
    }

    def goto_request(self):
        """
        Click <Finish and go to request>
        Goes to SCR_0115 (through the wait screen)
        """
        return self.go("go request")

    def goto_budget(self):
        """
        Click <Finish & edit budget>
        Goes to SCR_0006
        """
        return self.go("go budget")