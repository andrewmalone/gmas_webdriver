from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath

class SCR0233(Page):
    """
    SCR_0233 Subagreement home
    """
    locators = {
        "documents": "link=Documents",
        "budget": "event=ViewSubagreementIssuedBudgetEvent",
        "amendment": "event=ViewAmendmentEvent",
        "amendment row": xpath.parent_row_of_event("ViewAmendmentEvent")
    }

    @property
    def amendment_count(self):
        """
        Number of amendments
        """
        return len(self.finds("amendment"))

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def goto_budget(self):
        """
        Clicks the <Subagreement detailed budget> button
        Goes to SCR_0428
        """
        return self.go("budget")

    def amendment(self, number):
        """
        Returns the nth amendment row
        //Amendment_row
        """
        row = self.finds("amendment row")[number - 1]
        return self.Amendment_row(row, self)

    class Amendment_row(Row):
        locators = {
            "link": "event=ViewAmendmentEvent"
        }

        def go(self):
            """
            Clicks the amendment link
            Goes to SCR_0240
            """
            return self._go("link")


