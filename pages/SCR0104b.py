from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath



class SCR0104b(Page):
    """
    SCR_0104b Segment Home
    """

    
    locators = {
    "make revision": 'css=a[href*=SegmentHomeMakeRevisionEvent]',
    "continue revision": "css=a[href*='SegmentHomeEditRevisionEvent']",
    "confirm research team": "css=img[alt='Confirm research team']",
    "create request": "css=a[href*='SegmentHomeCreateRequestEvent']",
    "documents": "event=RepositoryLinkEvent",
    "document count": "xpath=(//a[contains(@href,'RepositoryLinkEvent')])[1]/ancestor::tr[1]/td[4]",
    "approvals": "event=ApprovalListHomeEvent",
    "notices": "event=ViewNoticeListEvent",
    "subagreements": "event=SubagreementsLinkEvent",
    "research team": "event=ResearchStaffLinkEvent",
    "admin team": "css=a[href*=SegmentSummaryAdministrativeTeamLinkEvent]",
    "requests": "css=a[href*=RequestListEvent]",
    "accounts": "event=AccountsLinkEvent",
    "segment documents": "event=SegmentDocumentsLinkEvent",
    "revisions": "event=SegmentHomeRevisionListEvent",
    "event history": "event=SegmentSummaryViewProjectHistoryLinkEvent",
    "todos": "event=SegmentSummaryViewProjectToDosLinkEvent",
    "project_info": xpath.text_sibling("td", "Project Information", 2),
    "dates_dollars": "event=SegmentHomeViewDatesAndDollarsEvent",
    "additional info": "event=AdditionalAwardInformationEvent",
    "fin award info": "event=FinancialAwardInformationEvent",
    "obligated dates": xpath.text_sibling("td", "Obligated dates", 2),
    "anticipated dates": xpath.text_sibling("td", "Anticipated dates", 2),
    "dates_dollars direct": "xpath=//td[contains(text(), 'Obligated ($.00)')]/ancestor::table[1]//tr[@class='bg0'][position()=5]",
    "dates_dollars indirect" : "xpath=//td[contains(text(), 'Obligated ($.00)')]/ancestor::table[1]//tr[@class='bg0'][position()=6]",
    "dates_dollars total": "xpath=//td[contains(text(), 'Obligated ($.00)')]/ancestor::table[1]//tr[@class='bg0'][position()=7]",
    "open all": "link=open all",
    "new segment home": "xpath=//a[contains(@href, '/gmas/project/SCR0104SegmentHome')]"
    
    }

    _locators = {
                 
    "obligated dates": "xpath=//table[@id='segmentDatesGrid']/tbody/tr/td[2]",
    "anticipated dates": "xpath=//table[@id='segmentDatesGrid']/tbody/tr[2]/td[2]",
    "dates_dollars direct": "xpath=//table[@id='segmentDollarsGrid']/tbody/tr[2]",
    "dates_dollars indirect" : "xpath=//table[@id='segmentDollarsGrid']/tbody/tr[3]",
    "dates_dollars total": "xpath=//table[@id='segmentDollarsGrid']/tbody/tr",
    }
      
      
      
    obligated_dates = RText("obligated dates", "Obligated dates")
    anticipated_dates = RText("anticipated dates", "Anticipated dates")

#     @property
#     def document_count(self):
#         """
#         Number of documents showing in the document component
#         """
#         count = self.find("document count").text
#         return int(count[:count.find(" ")])

#     @property
#     def status(self):
#         """
#         Segment status
#         """
#         text = self.find("project_info").text
#         return text[text.index("|") + 2:]
    
    def segment_home(self):
        try:
            return self.go("new segment home")
        except:
            self.find("open all").click()
            return self
        
        
#     @classmethod
#     def url(self, segment_id):
#         """
#         Direct navigation to a segment home (based on segment id)
#         """
#         url = "https://%s.harvard.edu/gmas/project/SCR0104SegmentHome.jsp?segmentId=%s" % (self.env, segment_id)
#         self.driver.get(url)
#         return SCR0104b(self.driver)

    @classmethod
    def url(cls, segment_id, project_id):
        """
        Direct navigation to segmenthome
        """
        url = "{{}}/gmas/dispatch?ref=%2Fuser%2FSCR0270GMASHomePage.jsp&segmentId={}&formName=SegmentHomeForm&projectId={}&ProjectListSegmentHomeEvent"
        return url.format( segment_id, project_id)

#     def make_revision(self):
#         """
#         Click the <Make revision> button
#         Goes to SCR_0105 (through the wait screen)
#         """
#         #self.driver.find_element_by_css_selector(locators["make revision"]).click()
#         self.find_element(locators["make revision"]).click()
#         self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0105]"))
#         from pages.SCR0105 import SCR0105
#         return SCR0105(self.driver)
# 
#     def create_request(self):
#         """
#         Clicks the <Create request> button
#         Goes to SCR_0472
#         """
#         return self.go("create request")


  

        

    def continue_revision(self):
        """
        Clicks the "continue making changes" link for an open revision
        Goes to SCR_0105
        """
        self.find("continue revision").click()
        return self.load_page()

    def confirm_research_team(self):
        """
        Clicks the <Confirm research team> button
        Goes to SCR_0645
        """
        return self.go("confirm research team")

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def goto_dates_dollars(self):
        """
        Clicks the "Dates and Dollars" link
        Goes to SCR_0070
        """
        return self.go("dates_dollars")

    def goto_additional_info(self):
        """
        Clicks the "Additional award information" link
        Goes to SCR_0519
        """
        return self.go("additional info")

    def goto_approvals(self):
        """
        Clicks the "Approvals" link
        Goes to SCR_0080
        """
        return self.go("approvals")

    def goto_notices(self):
        """
        Clicks the "Sponsor notices" link
        Goes to SCR_0308
        """
        return self.go("notices")

    def goto_subagreements(self):
        """
        Clicks the "Subagreements" link
        Goes to SCR_0232
        """
        return self.go("subagreements")

    def goto_research_team(self):
        """
        Clicks the "Research staff" link
        Goes to SCR_0015
        """
        return self.go("research team")

    def goto_admin_team(self):
        """
        Clicks the "Administrative team" link
        Goes to SCR_0300
        """
        return self.go("admin team")

    def goto_requests(self):
        """
        Clicks the "Requests" link
        Goes to SCR_0344
        """
        return self.go("requests")

    def goto_accounts(self):
        """
        Clicks the "Accounts" link
        Goes to SCR_0360
        """
        return self.go("accounts")

    def goto_segment_documents(self):
        """
        Clicks the "Segment documents" link
        Goes to SCR_0634
        """
        return self.go("segment documents")

    def goto_revisions(self):
        """
        Clicks the "Revisions" link
        Goes to SCR_0425
        """
        return self.go("revisions")

    def goto_event_history(self):
        """
        Clicks the "Event history" link
        Goes to SCR_0002
        """
        return self.go("event history")

    def goto_todos(self):
        """
        Clicks the "Segment to-do's" link
        Goes to SCR_0159
        """
        return self.go("todos")
     
    def open_all(self):
        """
        Click the open all 
        """
        self.find("open all").click()
        
#     @property
#     def new_segment(self):
#         """
#         Click the new segment home link 
#         """
#         return self.go("new segment home")
    

    def goto_financial_award_info(self):
        """
        Clicks the "Financial award information" link
        Goes to SCR_0647
        """
        return self.go("fin award info")
    
    @property
    def dates_dollars_direct(self):
        """
        List of all rows from the "dates and dollars" table
        """
        return [self.Dates_dollars_direct(row, self) for row in self.finds("dates_dollars direct")]
    
    class Dates_dollars_direct(Row):
        locators = {
            "type": Row.cell(2),
            "obligated": Row.cell(6),
            "anticipated": Row.cell(10),
            "expenses": Row.cell(14),
            "balance": Row.cell(18)
        }
        
        _locators = {
            "type": Row.cell(1),
            "obligated": Row.cell(2),
            "anticipated": Row.cell(3),
            "expenses": Row.cell(4),
            "balance": Row.cell(5)
        }
        
        type = RText("type", "Type")
        obligated = RText("obligated", "Obligated")
        anticipated = RText("anticipated", "Anticipated")
        expenses = RText("expenses", "Expenses")
        balance = RText("balance", "Balance")
        
    @property
    def dates_dollars_indirect(self):
        """
        List of all rows from the "dates and dollars" table
        """
        return [self.Dates_dollars_indirect(row, self) for row in self.finds("dates_dollars indirect")]
    
    class Dates_dollars_indirect(Row):
        locators = {
            "type": Row.cell(2),
            "obligated": Row.cell(6),
            "anticipated": Row.cell(10),
            "expenses": Row.cell(14),
            "balance": Row.cell(18)
        }
        
        _locators = {
            "type": Row.cell(1),
            "obligated": Row.cell(2),
            "anticipated": Row.cell(3),
            "expenses": Row.cell(4),
            "balance": Row.cell(5)
        }
        
        type = RText("type", "Type")
        obligated = RText("obligated", "Obligated")
        anticipated = RText("anticipated", "Anticipated")
        expenses = RText("expenses", "Expenses")
        balance = RText("balance", "Balance")
        
    @property
    def dates_dollars_total(self):
        """
        List of all rows from the "dates and dollars" table
        """
        return [self.Dates_dollars_total(row, self) for row in self.finds("dates_dollars total")]
    
    class Dates_dollars_total(Row):
        locators = {
            "type": Row.cell(2),
            "obligated": Row.cell(6),
            "anticipated": Row.cell(10),
            "expenses": Row.cell(14),
            "balance": Row.cell(18)
        }
        
        _locators = {
            "type": Row.cell(1),
            "obligated": Row.cell(2),
            "anticipated": Row.cell(3),
            "expenses": Row.cell(4),
            "balance": Row.cell(5)
        }
        
        type = RText("type", "Type")
        obligated = RText("obligated", "Obligated")
        anticipated = RText("anticipated", "Anticipated")
        expenses = RText("expenses", "Expenses")
        balance = RText("balance", "Balance")

