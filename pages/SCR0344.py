from pages.Page import Page
from pages.elements import Row


class SCR0344(Page):
    """
    SCR_0344 Request list
    """
    locators = {
        "request row": "xpath=//a[contains(@href,'RequestListLinkEvent')]/ancestor::tr[1]",
        "request row id": "xpath=//a[contains(@href,'requestId=REPLACE')]/ancestor::tr[1]"
    }

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

    class request_row(Row):
        locators = {
            "link": "css=a[href*=RequestListLinkEvent]"
        }

        def go(self):
            """
            Clicks the request link
            Goes to SCR_0115
            """
            return self._go("link")
