from pages.Page import Page, GMWebElement
from pages.elements import Checkbox

class SCR0196(Page):
    """
    SCR_0196 Edit accounts in revision
    """
    locators = {
        "add account": "name=AddAccountRevisionEvent",
        "ok": "name=EditAccountsSaveChangesEvent",
        "account name": "link=REPLACE",
        "account": "css=a[href*=viewDescription]",
        "account row": "xpath=//a[contains(@href,'viewDescription')]/../..",
        "next": "EditAccountsNextEvent"
    }

    class account_row(GMWebElement):
        """
        Subclass for an individual account row on SCR_0196
        """
        locators = {
            "checkbox": "css=input[type=checkbox]",
            "link": "css=a[href*=viewDescription]"
        }

        checkbox = Checkbox("checkbox", "Checkbox to send a validated account to the GL")

        def __init__(self, row, page):
            self.driver = row
            self.page = page

        def go(self):
            """
            Click the account's link
            Goes to SCR_0474
            """
            self.find("link").click()
            return self.page.load_page()

    def account(self, n):
        """
        Returns the nth account row object:
        //account_row

        Example: Edit the second account on the screen - `p = p.account(2).go()`
        """
        return self.account_row(self.finds("account row")[n - 1], self)

    def add_account(self):
        """
        Click <Add account>
        Goes to SCR_0474
        """
        return self.go("add account")

    def ok(self):
        """
        Click <Done making changes to this section>
        Goes to SCR_0105
        """
        return self.go("ok")

    def next(self):
        """
        Click <Next>
        Goes to SCR_0427
        """
        return self.go("next")

    def edit_account(self, account):
        """
        Click an account link. `account` can be a string or a positive integer
        * string: clicks the link matching the passed string `p = p.edit_account('Main 1')`
        * integer: clicks the nth account link (counting starts at 1). `p = p.edit_account(2)` clicks the second account on the page

        Goes to SCR_0474
        """
        if type(account) is str:
            return self.go("account name", account)
        if type(account) is int and account > 0:
            self.finds("account")[account - 1].click()
            return self.load_page()

