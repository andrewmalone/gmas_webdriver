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
    if not (p.scr == "SCR0025" and p.huid == huid):
        # Search for the person
        p = search_by_huid(p, huid)
    if p.user_flag != flag:
        # Flag the user if the flag isn't already what we want
        p = p.edit_user()
        p.user_flag = flag
        p = p.ok()
    return p



class SecondPage(BasePage):
    
    def _verify_page(self):
         try:
             self.wait_for_element_visibility(10,"xpath","//a[contains(@href,'PersonProfileViewTeamEvent')][contains(text(),'REPLACE')]")
         except:
             raise IncorrectPageException
     
     
     
    def add_to_project_team(p, huid, segment_id, role):[ submit page ]
    
    import second page
    Second_page_obj = SecondPage(self.driver)
    Second_page_obj.submit_requestpage()
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

