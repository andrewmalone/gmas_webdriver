from pages.Page import Page
from pages.elements import Row


class SCR0406(Page):
    """
    SCR_0406 Request submissions
    """
    locators = {
        "submission rows": "css=table.bg0 tr.bg0",
    }

    @property
    def submission_count(self):
        """
        Number of submissions
        """
        return len(self.finds("submission rows"))

    def submission(self, n):
        """
        Returns the Nth submission
        //Submission_row
        """
        row = self.finds("submission rows")[n - 1]
        return self.Submission_row(row, self)

    class Submission_row(Row):
        locators = {
            "tracking number": "event=TrackingNumberForwardEvent",
            "submission image": "event=RequestSubmissionDocumentDisplayEvent"
        }

        def goto_tracking(self):
            """
            Clicks the Grants.gov tracking number
            Goes to SCR_0618
            """
            return self._go("tracking number")

        def goto_image(self):
            """
            Clicks the Grants.gov application image
            Goes to SCR_0406a
            """
            return self._go("submission image")
