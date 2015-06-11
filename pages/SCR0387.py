from pages.Page import Page
from pages.elements import Row, RText, Radio


class SCR0387(Page):
    """
    SCR_0387 Associate requests to notice
    """
    locators = {
        "next": "name=IdentifyRequestsForNoticeNextEvent",
        "request row": "xpath=//a[contains(text(), 'Request title')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>2]"
    }
    _locators = {
        "request row": "css=[id$=associatedRequestsFieldset] tbody tr"
    }

    def check_first(self):
        """
        Checks the first request on the page
        """
        self.find_element("css=input[type=checkbox]").click()

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0083
        """
        return self.go("next")

    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0387
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FButtonsBar.jsp&segmentId={}&formName=SegmentHomeForm&SegmentHomeLogNoticeEvent"
        return url.format(segment_id)

    @property
    def requests(self):
        """
        List of request rows
        """
        return [self.Request_row(row, self) for row in self.finds("request row")]

    class Request_row(Row):
        locators = {
            "checkbox": Row.cell(1),
            "request title": Row.cell(4),
            "request type": Row.cell(8),
            "proposed dates": Row.cell(12),
            "proposed dollars": Row.cell(16),
            "date submitted": Row.cell(20),
            "status": Row.cell(24)
        }
        _locators = {
            "checkbox": Row.cell(1),
            "request title": Row.cell(2),
            "request type": Row.cell(3),
            "proposed dates": Row.cell(4),
            "proposed dollars": Row.cell(5),
            "date submitted": Row.cell(6),
            "status": Row.cell(7)
        }

        checkbox = Radio("Checkbox", "Check box")
        request_title = RText("request title", "Request title")
        request_type = RText("request type", "Request type")
        proposed_dates = RText("proposed dates", "Proposed dates")
        proposed_dollars = RText("proposed dollars", "Proposed dollars")
        date_submitted = RText("date submitted", "Date submitted")
        status = RText("status", "Status")
