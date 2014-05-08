from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0250(Page):
    """
    SCR_0250 Subagreement list for request
    """
    locators = {
        "sub link": "event=SubagreementEvent",
        "sub row": xpath.parent_row_of_event("SubagreementEvent")
    }

    @property
    def sub_count(self):
        """
        Count of subagreements shown on the page
        """
        return len(self.finds("sub link"))

    def sub(self, n):
        """
        Returns the row for the nth sub on the page
        //Subagreement_row
        """
        row = self.finds("sub row")[n - 1]
        return self.Subagreement_row(row, self)

    class Subagreement_row(Row):
        locators = {
            "link": "event=SubagreementEvent",
            "status": "css=td:nth-child(11)"
        }

        status = RText("status", "Subagreement status")

        def go(self):
            """
            Clicks the subagreement link
            Goes to SCR_0450 or SCR_0233
            """
            return self._go("link")
