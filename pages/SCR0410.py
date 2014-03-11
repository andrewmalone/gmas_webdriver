from pages.Page import Page


class SCR0410(Page):
    """
    SCR_0410 Indirect Costs
    """
    locators = {
        "excluded": "event=ViewIndirectCostViewExclusionsEvent"
    }

    def goto_exclusions(self):
        """
        Click "Costs not subject to overhead"
        Goes to SCR_0164
        """
        return self.go("excluded")