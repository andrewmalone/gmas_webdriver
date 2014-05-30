from pages.Page import Page


class SCR0410(Page):
    """
    SCR_0410 Indirect Costs
    """
    locators = {
        "excluded": "event=ViewIndirectCostViewExclusionsEvent",
        "next period": "css=input[title='Next period']",
        "periods": "xpath=//td[@class='strong'][contains(text(),'Period')]"
    }

    @property
    def period_count(self):
        """
        Total number of budget periods
        """
        return self.find("periods").text[12]

    @property
    def current_period(self):
        """
        Current budget period
        """
        return self.find("periods").text[7]

    def goto_exclusions(self):
        """
        Click "Costs not subject to overhead"
        Goes to SCR_0164
        """
        return self.go("excluded")

    def next(self):
        """
        Click the next period button
        """
        return self.go("next period")
