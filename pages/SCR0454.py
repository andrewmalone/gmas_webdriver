from pages.Page import Page
from pages.elements import Row, RText, Radio
import utilities.xpath as xpath



class SCR0454(Page):
    """
    SCR_0454 Edit notice associations
    """
    locators = {
#        "request row": "xpath=//*[contains(normalize-space(text()), 'Request title')]/ancestor::tr[1]/following-sibling::tr[3]"
        "request row": "xpath=//a[contains(text(), 'Request title')]/ancestor::table[1]//tr[4]"
       
    }

    @classmethod
    def url(cls, segment_id, notice_id, version):
        """
        Direct navigation to SCR_0454
        """
        url = "{{}}/gmas/dispatch?&segmentId={}&noticeId={}&version={}&EditRequestNoticeAssociationEvent.x=88&EditRequestNoticeAssociationEvent.y=2&ref=%2Fnotice%2FSCR0309NoticeDetailsInclude.jsp&formName=NoticeForm"
        return url.format(segment_id, notice_id, version)
    
    def request(self, n):
        """
        Returns the nth request in the list
        //Request_row
        """
        row = self.finds("request row")[n - 1]
        return self.Request_row(row, self) 
    
    @property
    def requests(self):
        """
        Returns the nth request in the list
        //Request_row
        """
        return [self.Request_row(row, self) for row in self.finds("request row")]
    
    class Request_row(Row):
        locators = {
            "check box": Row.cell(1),
            "request title": Row.cell(4),
            "request type": Row.cell(8),
            "proposed dates": Row.cell(12),
            "proposed dollars": Row.cell(16),
            "date submitted": Row.cell(20),
            "status": Row.cell(24)
        }
        check_box = Radio('Check box', 'Check box')
        request_title = RText('request title', 'Request title')
        request_type = RText('request type', 'Request type')
        proposed_dates = RText('proposed dates', 'Proposed date')
        proposed_dollars = RText('proposed dollars', 'Proposed dollars')
        date_submitted = RText('date submitted', 'Date submitted')
        status = RText('status', 'Status')

