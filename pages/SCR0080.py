from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


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

        def go(self):
            """
            Click the approval link
            Goes to SCR_0081
            """
            return self._go("link")
