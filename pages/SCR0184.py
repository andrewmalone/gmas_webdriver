from pages.Page import Page
from pages.elements import Select, Text


class SCR0184(Page):
    """
    SCR_0184 Create Fund
    """
    locators = {
        "cancel": "name=CreateFundCancelEvent",
        "ok": "CreateFundOKEvent",
        "fund_type": "fundType",
        "fund": "fundValue"
    }

    fund_type = Select("fund_type", "Fund type")
    fund = Text("fund", "Fund value")

    def cancel(self):
        """
        Click <Cancel>
        Goes to SCR_0474
        """
        return self.go("cancel")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0474
        """
        return self.go("ok")
