from pages.Page import Page
from pages.elements import Text, Select, Radio, Row


class SCR0020(Page):
    """
    SCR_0020 Indirect cost entry
    """
    locators = {
        "ok": "name=SelectIndirectCostRateOKEvent",
        "policy": "css=input[name=rateType]",
        "rate_row": "xpath=//input[contains(@name,'RateList__')][@class='yearinput']/ancestor::tr[1]"
    }

    rate_policy = Radio("policy", "IDC Rate Policy", mapping={
        "single": "SingleRatePolicy",
        "fiscal": "RateByFiscalYearPolicy",
        "budget": "RateByBudgetPeriodPolicy"
        })

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0018
        """
        return self.go("ok")

    @property
    def rate_count(self):
        """
        Number of rates
        """
        return len(self.finds("rate_row"))

    def rate(self, n):
        """
        Returns the nth rate row from the page
        //Rate
        """
        row = self.finds("rate_row")[n - 1]
        return self.Rate(row, self)

    class Rate(Row):
        locators = {
            "rate": "css=input[type=text][name*=RateList__]",
            "type": "css=select[name$='__idcTypeId']"
        }

        rate = Text("rate", "IDC Rate edit box")
        rate_type = Select("type", "Rate type (dropdown)")
