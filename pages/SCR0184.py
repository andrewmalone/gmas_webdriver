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
        "fund": "fundValue",
        "get_new_fund": "GetNewFundForCreateEvent"
    }

    fund_type = Select("fund_type", "Fund type")
    fund = Text("fund", "Fund value")

    def get_new_fund(self):
        """
        Click <Get new fund>
        """
        return self.go("get_new_fund")

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
