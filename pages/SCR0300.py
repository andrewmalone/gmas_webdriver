from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0300(Page):
    """
    SCR_0300 Admin team
    """
    locators = {
        "role": "link=REPLACE",
        "row by person": "xpath=//a[contains(@href,'ProjectAdminTeamPersonProfileEvent')][contains(@href,'personId=REPLACE')]/ancestor::tr[1]",
        "row by role": "xpath=//*[contains(text(),'REPLACE')][not(@class)]/ancestor::tr[1]",
        "row": xpath.parent_row_of_event("ProjectAdminTeamEditRolesEvent"),
        "add": "ProjectAdminTeamAddRolesEvent",
        "administrative team": "xpath=//*[contains(@href, 'Role')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>2]"
        
    }

    @classmethod
    def url(cls, segmentId):
        """
        Direct navigation to SCR_0300
        """
        url = "{{}}/gmas/dispatch?segmentId={}&formName=SegmentHomeForm&SegmentSummaryAdministrativeTeamLinkEvent="
        return url.format(segmentId)
 
    
    @property
    def row_count(self):
        """
        Count of rows that can be clicked (not PI)
        """
        return len(self.finds("row"))
 
    def row(self, n):
        """
        Returns the nth row (that has a clickable row)
        //role_row
        """
        row = self.finds("row")[n - 1]
        return self.role_row(row, self)
 
    def goto_role(self, role):
        """
        Clicks the first matching role link (exact match)
        Goes to SCR_0301
        """
        return self.go("role", role)
 
    def role_rows(self, role=None):
        """
        Returns a list of rows matching the role specified. If no role is specified, returns all rows with a clickable row (so not PI)
        //role_row
        """
        if role is None:
            elements = self.finds("row")
        else:
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
#     
    @property
    def row(self):
        """
        List of all rows from the "Project administrative team" table
        """
        return [self.Row(row, self) for row in self.finds("administrative team")]
    
    class Row(Row):
        locators = {
            "role":  Row.cell(3),
            "name":  Row.cell(7),
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