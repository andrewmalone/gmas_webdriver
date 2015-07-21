from pages.Page import Page
from pages.elements import Row
from pages.elements import RText
import utilities.xpath as xpath
import utilities.url as url


class SCR0080(Page):
    """
    SCR_0080 Approval List
    """
    locators = {
        "approval link": "event=ApprovalListViewOrEditDetailEvent",
        "approval row": xpath.parent_row_of_event("ApprovalListViewOrEditDetailEvent")
    }


    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0015
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&segmentId={}&ApprovalListHomeEvent=&formName=SegmentHomeForm"
        return url.format(segment_id)

    @property
    def approval_count(self):
        """
        Count of approvals in the list
        """
        return len(self.finds("approval link"))

    def goto_first_approval(self):
        """
        Click the first approval in the list
        """
        # TODO - document which pages here
        return self.go("approval link")

    @property
    def approvals(self):
        """
        List of all approval row objects
        """
        approvals = []
        for row in self.finds("approval row"):
            approvals.append(self.Approval_row(row, self))
        return approvals

    def approval(self, n):
        """
        Returns the nth approval
        //Approval_row
        """
        row = self.finds("approval row")[n - 1]
        return self.Approval_row(row, self)

    class Approval_row(Row):
        locators = {
            "link": "event=ApprovalListViewOrEditDetailEvent",
            "status": Row.cell(3),
            "approval type": Row.cell(7),
            "resp. party": Row.cell(11),
            "due date": Row.cell(15),
            "effective": Row.cell(19),
            "expires": Row.cell(23),
            "m": Row.cell(27),
            "c": Row.cell(31)
        }
        
        status = RText("status", "Status")
        approval_type = RText("approval type", "Approval type")
        resp_party = RText("resp. party", "Resp. party")
        due_date = RText("due date", "Due date")
        effective = RText("effective", "Effective")
        expires = RText("expires", "Expires")
        m = RText("m", "M")
        c = RText("c", "C")

        @property
        def type(self):
            """
            Approval type
            """
            return self.find("link").text

        @property
        def status(self):
            """
            Approval status
            """
            return self.cell_text(3)

        @property
        def huid(self):
            """
            HUID for the approval (if it is a person approval)
            """
            link = self.find("link").get_attribute("href")
            return url.url_param(link, "HUID")

        @property
        def approval_id(self):
            """
            Approval ID (from the url)
            """
            link = self.find("link").get_attribute("href")
            return url.url_param(link, "approvalId")

        def go(self):
            """
            Click the approval link
            Goes to SCR_0081
            """
            return self._go("link")
        
    
