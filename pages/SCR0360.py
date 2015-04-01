from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


class SCR0360(Page):
    """
    SCR_0360 Account list
    """
    locators = {
        "account row": xpath.parent_row_of_event("ViewAccountDetailsEvent")
    }

    @property
    def account_count(self):
        """
        Number of accounts
        """
        return len(self.finds("account row"))

    def account(self, num):
        """
        Returns an account row
        //account_row
        """
        return self.account_row(self.finds("account row")[num - 1], self)

    class account_row(Row):
        locators = {
            "link": "event=ViewAccountDetailsEvent"
        }

        def go(self):
            """
            Clicks the account link
            Goes to SCR_0187
            """
            return self._go("link")
