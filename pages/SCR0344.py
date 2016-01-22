from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath



class SCR0344(Page):
    """
    SCR_0344 Request list
    """
    locators = {
        "request row": "xpath=//a[contains(@href,'LinkEvent')]/ancestor::tr[1]",
        "request row id": "xpath=//a[contains(@href,'requestId=REPLACE')]/ancestor::tr[1]"
    }
    
    @classmethod
    def url(cls, segment_id,):
        """
        Direct navigation to SCR_0426
        """
        url = "{{}}/gmas/dispatch?ref=%2Ftemplates%2Fcommon%2FsegmentNavigation.xhtml&segmentId={}&RequestListEvent=&formName=SegmentHomeForm"
        return url.format(segment_id,)

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

    class request_row(Row):
        locators = {
            "link": "css=a[href*=LinkEvent]",
            "request id": Row.cell(3),
            "title": Row.cell(7),
            "type": Row.cell(11),
            "status": Row.cell(15),
            "due": Row.cell(19),
            "requested amount": Row.cell(23)
        }
        
        request_id = RText("request id", "Request ID")
        title = RText("title", "Title")
        type = RText("type", "Type")
        status = RText("status", "Status")
        due = RText("due", "Due")
        requested_amount = RText("requested amount", "Requested amount")
        
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
