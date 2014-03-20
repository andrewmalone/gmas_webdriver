from pages.Page import Page


class SCR0524(Page):
    """
    SCR_0524 Edit organization chart ranges
    """
    locators = {
        "cancel": "EditChartOfAccountsAttributeCancelEvent"
    }

    def cancel(self):
        """
        Click <Cancel>
        Goes to SCR_0134a
        """
        return self.go("cancel")
