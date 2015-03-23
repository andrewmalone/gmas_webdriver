from pages.Page import Page
from pages.elements import Row


class SCR0560(Page):
    """
    SCR_0560 GL History for IDC Rate
    """
    locators = {
        "rate_row": "xpath=//td[contains(text(), 'Account indirect cost rates')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
        "history_row": "xpath=//td[contains(text(), 'History of general ledger feeds')]/ancestor::table[1]//tr[@class='bg0'][position()>1]"
    }

    @property
    def rate_row_count(self):
        """
        Number of rows in the "Account indirect cost rates" table
        """
        return len(self.finds("rate_row"))

    def rate_row(self, n):
        """
        Returns the nth row from the "Account indirect cost rates" table
        //Rate_row
        """
        rows = self.finds("rate_row")
        return self.Rate_row(rows[n - 1], self)

    class Rate_row(Row):
        @property
        def rate(self):
            """
            IDC rate
            """
            return self.cell_text(2)

        @property
        def date(self):
            """
            IDC Effective date
            """
            return self.cell_text(6)
