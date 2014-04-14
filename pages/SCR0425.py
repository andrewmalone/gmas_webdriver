from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


class SCR0425(Page):
    """
    SCR_0425 Segment revision list
    """
    locators = {
        "revision row": xpath.parent_row_of_event("ListOfRevisionsAppliedRevisionDetailEvent")
    }

    @property
    def revision_count(self):
        """
        Number of revisions
        """
        return len(self.finds("revision row"))

    def revision(self, n):
        """
        Returns the nth revision row
        //Revision
        """
        row = self.finds("revision row")[n - 1]
        return self.Revision(row, self)

    class Revision(Row):
        locators = {
            "link": "event=ListOfRevisionsAppliedRevisionDetailEvent"
        }

        def go(self):
            """
            Click the revision link
            Goes to SCR_0426
            """
            return self._go("link")
