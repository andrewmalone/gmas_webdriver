from pages.Page import Page
from pages.elements import Row


class SCR0344(Page):
    """
    SCR_0344 Request list
    """
    locators = {
        "request row": "xpath=//a[contains(@href,'LinkEvent')]/ancestor::tr[1]",
        "request row id": "xpath=//a[contains(@href,'requestId=REPLACE')]/ancestor::tr[1]",
        "log_notice": "event=RequestListLogNoticeEvent"
    }

    @property
    def request_count(self):
        """
        Number of requests in the list
        """
        return len(self.finds("request row"))

    def request(self, num=None, request_id=None):
        """
        returns a request row based on index or id
        `p.request(1)` returns the first request
        `p.request(request_id=12345)` returns the request row for request id 12345
        //request_row
        """
        if request_id is None:
            row = self.finds("request row")[num - 1]
        else:
            row = self.find("request row id", request_id)
        return self.request_row(row, self)

    @property
    def requests(self):
        """
        List of request rows
        """
        return [self.request_row(row, self) for row in self.finds("request row")]

    def log_notice(self):
        return self.action("log_notice")

    class request_row(Row):
        locators = {
            "link": "css=a[href*=LinkEvent]"
        }

        @property
        def request_id(self):
            """
            Request ID
            """
            return self.cell_text(3)

        @property
        def type(self):
            """
            Request type
            """
            return self.cell_text(11)

        def go(self):
            """
            Clicks the request link
            Goes to SCR_0115
            """
            return self._go("link")
