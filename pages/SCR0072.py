from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath
import utilities.url as url

class SCR0072(Page):
    """
    SCR_0072 Account Financials
    """
    locators = {
        "people charged": "event=AccountFinancialsViewPersonnelExpensesEvent",
        "object": "event=AccountFinancialsViewTransactionDetailPerObjectCodeEvent",
        "object row": xpath.parent_row_of_event("AccountFinancialsViewTransactionDetailPerObjectCodeEvent"),
        "object row by object": "xpath=//a[contains(@href,'AccountFinancialsViewTransactionDetailPerObjectCodeEvent')][contains(@href, 'objectCode=REPLACE')]/ancestor::tr[1]"
    }

    def goto_people_charged(self):
        """
        Click "View people charged to this account"
        Goes to SCR_0471
        """
        return self.go("people charged")

    def object(self, object_code):
        """
        Returns an object code row based on index (int) or object code (string)
        //object_row
        """
        if type(object_code) is int:
            # get by index
            row = self.finds("object row")[object_code - 1]
        # use isinstance here to catch str or unicode
        if isinstance(object_code, basestring):
            # get by string
            row = self.find("object row by object", object_code)

        return self.object_row(row, self)

    def get_object_code_list(self):
        """
        Returns a list of object code links appearing on the screen
        """
        object_codes = []
        for elem in self.finds("object"):
            object_codes.append(url.url_param(elem.get_attribute("href"), "objectCode"))
        return object_codes

    def goto_object(self, object_code):
        """
        Clicks on a link for a specific object code
        `p.goto_object("6050")`
        Goes to SCR_0074

        This is a shortcut method - `p.goto_object("6050")` is equivalent to `p.object("6050").go()`
        """
        return self.object(object_code).go()

    class object_row(Row):
        locators = {
            "link": "css=a"
        }

        def go(self):
            """
            Clicks the object code link
            Goes to SCR_0074
            """
            return self._go("link")




