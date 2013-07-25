from pages.Page import Page


class SCR0018(Page):
    locators = {
        "ok": "name=IndirectCostCalculatorOKEvent",
        "select rate": "name=IndirectCostCalculatorSelectRateEvent"
    }

    def select_rate(self):
        # to SCR_0020
        return self.go("select rate")

    def ok(self):
        return self.go("ok")