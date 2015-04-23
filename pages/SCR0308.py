from pages.Page import Page
from pages.elements import Row, RText
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
    
    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0308
        """
        url = "{{}}/gmas/dispatch?ref=%2Fnotice%2FCOM0873NoticeSummary.jsp&ViewNoticeListEvent=&segmentId={}&formName=SegmentHomeForm&submit"
        return url.format(segment_id)

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
    
    @property
    def notices(self):
        """
        Returns the nth notice in the list
        //Notice_row
        """
        return [self.Notice_row(row, self) for row in self.finds("notice row")]
    
    class Notice_row(Row):
        locators = {
            "link": "event=ViewDetailsOfNoticeEvent",
            "title": Row.cell(3),
            "sponsor award no": Row.cell(7),
            "amendment": Row.cell(11),
            "date received": Row.cell(15),
            "status": Row.cell(19),
            "type": Row.cell(23)
        }

        def go(self):
            """
            Click the notice link
            Goes to SCR_0309
            """
            return self._go("link")
        title = RText("title", "Title")
        sponsor_award_no = RText("sponsor award no", "Sponsor award no")
        amendment = RText("amendment", "Amendment/modification no.")
        date_received = RText("date received", "Date received by Harvard")
        status = RText("status", "Status")
        type = RText("type", "Type")

        
