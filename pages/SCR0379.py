from pages.Page import Page
from pages.elements import Text


class SCR0379(Page):
    """
    SCR_0379 At risk details
    Only supports one account
    """
    locators = {
        "amount": "css=input[type=text][name$=atRiskMoney]",
        "start": "css=input[type=text][name$=atRiskStartDate]",
        "end": "css=input[type=text][name$=atRiskEndDate]",
        "finish": "EditRequestedAtRiskAccountsFinishEvent"
    }

    amount = Text("amount", "At-risk amount")
    start = Text("start", "Start date")
    end = Text("end", "End date")

    def ok(self):
        """
        Click <Finish>
        Goes to SCR_0115
        """
        return self.go("finish")