from pages.Page import Page
from pages.elements import Text, Select


class SCR0020(Page):
    """
    SCR_0020 Indirect cost entry
    {note}
    Currently only handles default 1 rate for full project
    {note}
    """
    locators = {
        "rate": "css=input[name$='__rateValue']",
        "type": "css=select[name$='__idcTypeId']",
        "ok": "name=SelectIndirectCostRateOKEvent"
    }

    rate = Text("rate", "IDC Rate edit box")
    rate_type = Select("type", "Rate type (dropdown)")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0018
        """
        return self.go("ok")
