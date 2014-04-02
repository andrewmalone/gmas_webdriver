from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


class SCR0308(Page):
    """
    SCR_0308 Notice list
    """
    locators = {
        "log notice": "name=LogNoticeEvent",
        "notice link": "css=a[href*='ViewDetailsOfNoticeEvent']",
        "notice row": xpath.parent_row_of_event("ViewDetailsOfNoticeEvent")
    }

    @property
    def notice_count(self):
        """
        Number of notices in the list
        """
        return len(self.finds("notice link"))

    def log_notice(self):
        """
        Click <Log notice>
        Goes to SCR_0387
        """
        return self.go("log notice")

    def goto_first_notice(self):
        """
        Click the first notice on the page
        Goes to SCR_0309
        """
        return self.go("notice link")

    def notice(self, n):
        """
        Returns the nth notice in the list
        //Notice_row
        """
        row = self.finds("notice row")[n - 1]
        return self.Notice_row(row, self)

    class Notice_row(Row):
        locators = {
            "link": "event=ViewDetailsOfNoticeEvent"
        }

        def go(self):
            """
            Click the notice link
            Goes to SCR_0309
            """
            return self._go("link")
