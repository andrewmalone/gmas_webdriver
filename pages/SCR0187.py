from pages.Page import Page


class SCR0187(Page):
    """
    SCR_0187 Account detail
    """
    locators = {
        "expenses": "event=ViewExpenseDetailsEvent",
        "gl history": "event=ViewGLHistoryEvent",
        "fund": "event=ViewFundDetailsEvent",
        "activity": "event=ViewActivityDetailsEvent",
        "subactivity": "event=ViewSubactivityDetailsEvent",
        "income": "event=IncomeEvent"
    }

    def goto_expenses(self):
        """
        Click the "Expenses" link
        Goes to SCR_0072
        """
        return self.go("expenses")

    def goto_gl_history(self):
        """
        Click the "View GL History" link
        Goes to SCR_0560
        """
        return self.go("gl history")

    def goto_fund(self):
        """
        Click the fund link
        Goes to SCR_0191
        """
        return self.go("fund")

    def goto_activity(self):
        """
        Click the activity link
        Goes to SCR_0192
        """
        return self.go("activity")

    def goto_subactivity(self):
        """
        Click the subactivity link
        Goes to SCR_0511
        """
        return self.go("subactivity")

    def goto_income(self):
        """
        Click the "Income" link
        Goes to SCR_0299
        """
        return self.go("income")