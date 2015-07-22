from pages.Page import Page
from pages.elements import Row
from pages.elements import RText
import utilities.xpath as xpath

class SCR0015(Page):
    """
    SCR_0015 Research team list

    This has only been tested with the request version of the screen. Also, there's no great way to go to a person by name (will be added eventually)
    """
    locators = {
        "add team member": "name=AddTeamMemberEvent",
        "PI link": "link=Principal Investigator",
        "edit team": "name=EditResearchTeamButton",
#         "person row": xpath.parent_row_of_event("ResearchPersonNameLinkEvent"),
        "research person row": "xpath=//table[@id='researchTeamDataTable']/tbody//tr[@class='bg0'][position()>0]",
        "non research person row": "xpath=//table[@id='nonResearchTeamDataTable']/tbody//tr[@class='bg0'][position()>1]",
        "person links": "event=ResearchPersonNameLinkEvent",
        "role links": "event=ResearchTeamMemberViewEvent"
    }

    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0015
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&ResearchStaffLinkEvent=&requestId=&segmentId={}&formName=SegmentHomeForm&requestFromPage=segmentPage&segmentResearchPerson=true"
        return url.format(segment_id)

    @property
    def people_count(self):
        """
        Number of people showing in the list
        """
        return len(self.finds("role links"))

    def add_team_member(self):
        """
        Click <Add team member>
        Goes to SCR_0252
        """
        return self.go("add team member")

    def goto_pi(self):
        """
        Click the "Principal investigator" link
        Goes to SCR_0363
        """
        return self.go("PI link")

    def goto_name(self, num):
        """
        Click the nth name on the screen
        Goes to SCR_0025
        """
        self.finds("person links")[num - 1].click()
        return self.load_page()

    def goto_role(self, num):
        """
        Click the nth role on the screen
        Goes to SCR_0363
        """
        self.finds("role links")[num - 1].click()
        return self.load_page()

    def edit_team(self):
        """
        Click the <Edit research team button>
        Goes to SCR_0649
        """
        return self.go("edit team")
    
    @property
    def research_person(self):
       return [self.Research_Person(row, self) for row in self.finds("research person row")]
   
   
    @property
    def nonResearch_person(self):
       return [self.NonResearch_Person(row, self) for row in self.finds("non research person row")]
   
    class Research_Person(Row):
        locators = {
            "name": Row.cell(2),
            "role": Row.cell(6),
            "key personnel": Row.cell(10),
            "investigator": Row.cell(14),
            "human subjects": Row.cell(18),
            "committed effort": Row.cell(22),
            "peoplesoft costing": Row.cell(26)
        }
        
        name = RText("name", "Research person Name")
        role = RText("role", "Role")
        Key_personnel = RText("key personnel", "Key personnel")
        investigator = RText("investigator", "Investigator")
        human_subjects = RText("human subjects", "Human subjects")
        committed_effort = RText("committed effort", "Committed effort")
        peoplesoft_costing = RText("peoplesoft costing", "Peoplesoft costing")
        
    class NonResearch_Person(Row):
        locators = {
            "name": Row.cell(2),
            "costing": Row.cell(5)
        }
        
        name = RText("name", "Non-Research person Name")
        costing = RText("costing", "Costing%")