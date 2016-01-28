from pages.Page import Page
from pages.elements import Row, RText, Text, Select
import utilities.xpath as xpath

class SCR0301(Page):
    """
    SCR_0301 Project Admin Role
    """
    locators = {
        "input": "xpath=//td[contains(text(),'REPLACE')]/ancestor::tr[1]//input",
        "remove": "RemoveSelectedPeopleFromRoleEvent",
        "row": xpath.parent_row_of_event("ProjectAdminTeamEditRolesEvent"),
        "add": "ProjectAdminTeamAddRolesEvent",
        "administrative team": "xpath=//*[contains(@href, 'Role')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>2]",
        "more details": "link=More details...",
        "admin team": "link=Administrative team"
    }
    
    _locators = {
        "administrative team": "xpath=//tbody[@id='editProjectAdministrativeTeamForm:projectAdministrativeTeamDatatable_data']/tr",
        "edit": "xpath=//button[@id='j_idt107:edit']"      
    }
    
    
    @classmethod
    def url(cls, segment_id, project_id):
        """
        Direct navigation to SCR_0301
        """
        url = "{{}}/gmas/dispatch?ref=%2Fuser%2FSCR0270GMASHomePage.jsp&segmentId={}&formName=SegmentHomeForm&projectId={}&ProjectListSegmentHomeEvent"
        return url.format(segment_id, project_id)
    
    def edit(self):
        try:
            return self.go("edit").click()
        except:
            return self
    
    def add(self):
        """
        Click <Add person to role>
        Goes to SCR_0051
        """
        return self.go("add")

    def remove(self):
        """
        Click <Remove selected people from role>
        """
        return self.go("remove")

    def select_name(self, name):
        """
        Selects a checkbox next to one of the names
        **note**: person id or huid are not available on this page, name is the best we can do for now
        """
        self.find("input", name).click()
        
    @property
    def row(self):
        """
        List of all rows from the "Project administrative team" table
        """
        return [self.Row(row, self) for row in self.finds("administrative team")]
    
    class Row(Row):
        locators = {
            "role":  Row.cell(3),
            "name":  Row.cell(7)
        }
        
        _locators = {
            "role":  Row.cell(1),
            "name":  Row.cell(2)
        }
        
        role = RText("role", "Role name")
        name = RText("name", "Person name")
