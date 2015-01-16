from scripts.person.search import search_by_huid
from abc import abstractmethod
from gmas_webdriver.pages.Page import Page

    
def flag_user(p, huid, flag):
    """
    Flag an HUID user as Yes/No (GMAS User flag)
    Starts from: any global screen
    Ends on: SCR_0025 person profile
    """
    # First check if we are on the person profile for the correct person
    if not (p.get_current_page()[0:7] == "SCR0025" and p.huid == huid):
        # Search for the person
        p = search_by_huid(p, huid)
    if p.user_flag != flag:
        # Flag the user if the flag isn't already what we want
        p = p.edit_user()
        p.user_flag = flag
        p = p.ok()
    return p



class BasePage(object):
    
    def __init__(self,driver):
        self.driver = driver
        self._verify_page()
        
    @abstractmethod
    def _verify_page(self):
        """
        THIS METHOD TELLS ME THAT IAM ON THIS BASEPAGE
        """



def add_to_standing_team(p, huid, team):
    """
    Adds a user to a standing team.
    Flags the user as "Yes" if not already flagged
    Starts from: any global screen
    Ends on: SCR_0050
    """
    # Check if the person is already a user
    p = flag_user(p, huid, "Yes")
    p = p.global_header.goto_people().goto_teams()
    p.name = team
    p = p.search().row(team).go().add_member()
    p.name = huid
    p = p.search()
    p.select_first()
    p = p.ok()
    return p

def remove_from_standing_team(p, huid, team):
    """
    Remove a user from a standing team.
    Starts from: any global screen
    Ends on: SCR_0050
    """
    p = search_by_huid(p, huid)
    person_id = p.get_person_id()
    p.open_all()
    p = p.goto_standing_team(team)
    p = p.goto_member(id=person_id)
    p = p.remove_member()
    return p

def add_to_project_team(p, huid, segment_id, role):
    """
    Adds a user to a project admin team
    Flags the user as "Yes" if not already flagged
    Starts from: Any global screen
    Ends on: SCR_0300
    """
    p = flag_user(p, huid, "Yes")
    p = p.goto_segment(segment_id).goto_admin_team()
    if len(p.role_rows(role)) == 0:
        import admin_team
        p = admin_team.add_role(p, role)
    p = p.goto_role(role).add()
    p.name = huid
    p = p.search()
    p.select_first()
    p = p.ok().goto_last_breadcrumb()
    return p

def remove_from_project_team(p, huid, segment_id, role=None):
    """
    Removes a user from a project admin team
    If role is specified, only that role is removed - otherwise the user is removed from all roles
    Starts from: Any global screen
    Ends on: SCR_0300
    """
    p = search_by_huid(p, huid)
    person_id = p.get_person_id()
    name = p.full_name
    p = p.goto_segment(segment_id).goto_admin_team()
    rows = p.person_rows(person_id)
    if len(rows) > 0:
        if role:
            p = p.goto_role(role)
            p.select_name(name)
            p = p.remove().goto_last_breadcrumb()
        else:
            while len(rows) > 0:
                p = rows[0].goto_role()
                p.select_name(name)
                p = p.remove().goto_last_breadcrumb()
                rows = p.person_rows(person_id)
    return p




class IncorrectPageException(Exception):
    """
    This Exception should be thrown when trying to instantiate the wrong Page
    
    """