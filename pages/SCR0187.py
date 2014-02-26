from pages.Page import Page


class SCR0187(Page):
    """
    SCR_0187 Account detail
    """
    locators = {
        "expenses": "event=ViewExpenseDetailsEvent"
    }

    def goto_expenses(self):
        """
        Click the "Expenses" link
        Goes to SCR_0072
        """
        return self.go("expenses")