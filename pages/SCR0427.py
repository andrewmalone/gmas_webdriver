from pages.Page import Page
from pages.elements import Text


class SCR0427(Page):
    """
    SCR_0427 Account allocation
    **Note**: currently only supports allocating to one account
    """
    locators = {
        "ok" : "name=AllocateAwardedFundstoAccountsDoneEvent",
        "allocation": "css=input[type=text][name$=__accountChangeAmount]"
    }

    allocation = Text("allocation", "Allocation change amount")

    def ok(self):
        """
        Click <Done making revisions to this section>
        Goes to SCR_0105
        """
        return self.go("ok")

