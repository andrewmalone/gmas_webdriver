from pages.Page import Page
from pages.elements import Row
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
            "link": "event=ApprovalListViewOrEditDetailEvent"
        }

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
