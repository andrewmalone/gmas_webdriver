from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


class SCR0287(Page):
    """
    SCR_0287 Role list
    """
    locators = {
        "role row": xpath.parent_row_of_event("ViewRoleEvent"),
        "next": "partial=Next"
    }

    def next(self):
        """
        Click "Next" link
        """
        return self.go("next")

    @property
    def role_count(self):
        """
        Number of roles on the page
        """
        return len(self.finds("role row"))

    def role(self, n):
        """
        Returns the nth role on the page
        //Role
        """
        row = self.finds("role row")[n - 1]
        return self.Role(row, self)

    class Role(Row):
        locators = {
            "link": "event=ViewRoleEvent"
        }

        def go(self):
            """
            Click the role link
            Goes to SCR_0288
            """
            return self._go("link")
