from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


class SCR0002(Page):
    """
    SCR_0002 Segment event history
    """
    locators = {
        "event row": xpath.parent_row_of_event("EventHistoryViewDetailsEvent")
    }

    @property
    def event_count(self):
        """
        Number of events on the screen (only those shown, not the total available through paging)
        """
        return len(self.finds("event row"))

    def event(self, n):
        """
        returns the nth event row
        //Event
        """
        row = self.finds("event row")[n - 1]
        return self.Event(row, self)

    class Event(Row):
        locators = {
            "link": "event=EventHistoryViewDetailsEvent"
        }

        def go(self):
            """
            Click the event link
            Goes to SCR_0260
            """
            return self._go("link")
