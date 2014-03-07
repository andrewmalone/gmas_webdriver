from pages.Page import Page
from pages.elements import Select

class SCR0074(Page):
    """
    SCR_0074 Account transactions
    """
    locators = {
        "period": "fixedChoice",
        "search": "TransactionDetailsSearchForTransactionsEvent"
    }

    time_period = Select("period", "Fixed time period dropdown")

    def view_transactions(self):
        """
        Click <View transactions> button
        """
        return self.go("search")