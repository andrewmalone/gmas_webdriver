from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0360(Page):
    """
    SCR_0360 Account list
    """
    locators = {
        "account row": xpath.parent_row_of_event("ViewAccountDetailsEvent"),
        "request new account": "xpath=//img[@title='Request New Account']",
        "request at-risk account": "xpath=//img[@title='Request At Risk Account']"
    }
    
    _locators = {
        "account row": xpath.parent_row_of_event("ViewAccountDetailsEvent")      
    }

    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0360
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&AccountsLinkEvent=&segmentId={}&formName=SegmentHomeForm"
        return url.format(segment_id)
    
    
    @property
    def account_count(self):
        """
        Number of accounts
        """
        return len(self.finds("account row"))

    def account(self, num):
        """
        Returns an account row
        //account_row
        """
        return self.account_row(self.finds("account row")[num - 1], self)

    @property
    def accounts(self):
        """
        List of account rows
        """
        return [self.account_row(row, self) for row in self.finds("account row")]

    class account_row(Row):
        locators = {
            "link": "event=ViewAccountDetailsEvent",
            "Group":Row.cell(2),
            "Description":Row.cell(6),
            "Year":Row.cell(10),
            "Type":Row.cell(14),
            "Auth tub":Row.cell(18),
            "Auth org":Row.cell(22),
            "Fund":Row.cell(26),
            "Activity":Row.cell(30),
            "Subactivity":Row.cell(34),
            "Auth root":Row.cell(38),
            "Status":Row.cell(42),
            "At risk":Row.cell(46)
        }
         
        _locators = {
            "link": "event=ViewAccountDetailsEvent",
            "Group":Row.cell(1),
            "Description":Row.cell(2),
            "Year":Row.cell(3),
            "Type":Row.cell(4),
            "Auth tub":Row.cell(5),
            "Auth org":Row.cell(6),
            "Fund":Row.cell(7),
            "Activity":Row.cell(8),
            "Subactivity":Row.cell(9),
            "Auth root":Row.cell(10),
            "Status":Row.cell(11),
            "At risk":Row.cell(12)
        } 
        
        def go(self):
            """
            Clicks the account link
            Goes to SCR_0187
            """
            return self._go("link")
        

        group = RText("Group", "Account group details")
        description = RText("Description", "Account description")
        year = RText("Year", "Account year details")
        type = RText("Type", "account type")
        auth_tub = RText("Auth tub", "Auth. tub details")
        auth_org = RText("Auth org", "Auth. org deatils")
        fund = RText("Fund", "fund details")
        activity = RText("Activity", "fund activity")
        subactivity = RText("Subactivity", "subactivity details")
        auth_root = RText("Auth root", "auth root deatils")
        status = RText("Status", "account status details")
        at_risk = RText("At risk", "at-risk account deatils")
            
