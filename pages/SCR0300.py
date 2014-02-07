from pages.Page import Page
from pages.elements import Row, RText

class SCR0300(Page):
    """
    SCR_0300 Admin team
    """
    locators = {
        "role": "link=REPLACE",
        "row by person": "xpath=//a[contains(@href,'ProjectAdminTeamPersonProfileEvent')][contains(@href,'personId=REPLACE')]/ancestor::tr[1]",
        "row by role": "xpath=//*[contains(text(),'REPLACE')][not(@class)]/ancestor::tr[1]",
        "add": "ProjectAdminTeamAddRolesEvent"
    }

    def goto_role(self, role):
        """
        Clicks the first matching role link (exact match)
        Goes to SCR_0301
        """
        return self.go("role", role)

    def role_rows(self, role):
        """
        Returns a list of rows matching the role specified
        //role_row
        """
        elements = self.finds("row by role", role)
        rows = []
        for el in elements:
            rows.append(self.role_row(el, self))
        return rows

    def person_rows(self, person_id):
        """
        Returns a list of rows matching the person specified (by person id)
        //role_row
        """
        elements = self.finds("row by person", person_id)
        rows = []
        for el in elements:
            rows.append(self.role_row(el, self))
        return rows

    def add_role(self):
        """
        Click <Add roles>
        Goes to SCR_0416
        """
        return self.go("add")

    class role_row(Row):
        locators = {
            "role": "css=td:nth-child(3)",
            "name": "css=td:nth-child(7)",
            "role link": "css=a[href*=ProjectAdminTeamEditRolesEvent]",
            "name link": "css=a[href*=ProjectAdminTeamPersonProfileEvent]"
        }

        role = RText("role", "Role name")
        name = RText("name", "Person name")

        def goto_role(self):
            """
            Click the role link
            Goes to SCR_0301
            """
            return self._go("role link")

        def person_id(self):
            """
            returns the person id for the current row
            """
            import urlparse
            element = self.find("name link")
            url = urlparse.urlparse(element.get_attribute("href"))
            query = urlparse.parse_qs(url.query)
            return query["personId"][0]