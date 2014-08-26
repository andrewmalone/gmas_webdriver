from pages.Page import Page
import utilities.xpath as xpath
from pages.elements import Row


class SCR0070(Page):
    """
    SCR_0070 Segment financials
    """
    locators = {
        "budget row": xpath.parent_row_of_event("SegmentFinancialsPeriodSummaryEvent")
    }

    @property
    def period_count(self):
        """
        Number of budget periods
        """
        return len(self.finds("budget row"))

    def period(self, n):
        """
        Returns the nth period row
        //Period_Row
        """
        row = self.finds("budget row")[n - 1]
        return self.Period_Row(row, self)

    class Period_Row(Row):
        locators = {
            "link": "event=SegmentFinancialsPeriodSummaryEvent"
        }

        def go(self):
            """
            Clicks the budget period link
            Goes to SCR_0071
            """
            return self._go("link")
