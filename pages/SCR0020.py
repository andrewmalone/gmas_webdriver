from pages.Page import Page
from pages.elements import Text, Select


class SCR0020(Page):
    locators = {
        "rate": "css=input[name$='__rateValue']",
        "type": "css=select[name$='__idcTypeId']",
        "ok": "name=SelectIndirectCostRateOKEvent"
    }

    rate = Text("rate")
    rate_type = Select("type")

    def ok(self):
        # to SCR_0018
        return self.go("ok")
