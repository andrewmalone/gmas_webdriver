from pages.Page import Page


class SCR0018(Page):
    """
    SCR_0018 Indirect Cost
    """
    locators = {
        "ok": "name=IndirectCostCalculatorOKEvent",
        "select rate": "name=IndirectCostCalculatorSelectRateEvent"
    }

    def select_rate(self):
        """
        Press the <Select rate> button
        Goes to SCR_0020
        """
        # to SCR_0020
        return self.go("select rate")

    def ok(self):
        """
        Press <Ok>
        Goes to SCR_0006
        """
        return self.go("ok")