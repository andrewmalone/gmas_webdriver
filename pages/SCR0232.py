from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath

class SCR0232(Page):
    """
    SCR_0232 Subagreement List
    """
    locators = {
        "subagreement link": "css=a[href*='SubagreementEvent']",
        "subagreement row":  xpath.parent_row_of_event("SubagreementEvent")
    }

    @property
    def sub_count(self):
        """
        Count of subagreements in the list
        """
        return len(self.finds("subagreement link"))

    def goto_first_subagreement(self):
        """
        Clicks the first subagreement link on the page
        Goes to SCR_0450 or SCR_0233
        """
        return self.go("subagreement link")

    def sub(self, number):
        """
        Returns the nth subagreement row on the page
        //Subagreement_row
        """
        row = self.finds("subagreement row")[number - 1]
        return self.Subagreement_row(row, self)

    class Subagreement_row(Row):
        locators = {
            "link": "event=SubagreementEvent",
            "status": "css=td:nth-child(15)"
        }

        status = RText("status", "Subagreement status")

        def go(self):
            """
            Clicks the subagreement link
            Goes to SCR_0450 or SCR_0233
            """
            return self._go("link")
    
