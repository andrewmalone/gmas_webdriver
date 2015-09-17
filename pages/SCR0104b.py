from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath
from selenium.webdriver.support.expected_conditions import title_contains



class SCR0104b(Page):
    """
    SCR_0104b Segment Home
    """
    locators = {
#     "make revision": 'css=a[href*=SegmentHomeMakeRevisionEvent]',
#     "continue revision": "css=a[href*='SegmentHomeEditRevisionEvent']",
#     "confirm research team": "css=img[alt='Confirm research team']",
#     "create request": "css=a[href*='SegmentHomeCreateRequestEvent']",
#     "documents": "event=RepositoryLinkEvent",
#     "document count": "xpath=(//a[contains(@href,'RepositoryLinkEvent')])[1]/ancestor::tr[1]/td[4]",
#     "approvals": "event=ApprovalListHomeEvent",
#     "notices": "event=ViewNoticeListEvent",
#     "subagreements": "event=SubagreementsLinkEvent",
#     "research team": "event=ResearchStaffLinkEvent",
#     "admin team": "css=a[href*=SegmentSummaryAdministrativeTeamLinkEvent]",
#     "requests": "css=a[href*=RequestListEvent]",
#     "accounts": "event=AccountsLinkEvent",
#     "segment documents": "event=SegmentDocumentsLinkEvent",
#     "revisions": "event=SegmentHomeRevisionListEvent",
#     "event history": "event=SegmentSummaryViewProjectHistoryLinkEvent",
#     "todos": "event=SegmentSummaryViewProjectToDosLinkEvent",
    "open all": "link=open all",
    "project_id": xpath.text_sibling("td", "Project Information", 2),
    "tub": xpath.text_sibling("td", "Tub", 2),
    "org": xpath.text_sibling("td", "Org", 2),
    "nickname": xpath.text_sibling("td", "Nickname", 2),
    "project type": xpath.text_sibling("td", "Project type", 1),
    "AARA funding": xpath.text_sibling("td", "ARRA(Stimulus)funding?", 1),
    "funding instrument": xpath.text_sibling("td", "Funding instrument", 1),
    "award number": xpath.text_sibling("td", "Award number", 1),
    "sponsor type": xpath.text_sibling("td", "Sponsor type", 1),
    "prime sponsor type": xpath.text_sibling("td", "Prime sponsor type", 1),
    "prime PI": xpath.text_sibling("td", "Prime Institute PI", 1)
#     "dates_dollars": "event=SegmentHomeViewDatesAndDollarsEvent",
#     "additional info": "event=AdditionalAwardInformationEvent",
#     "fin award info": "event=FinancialAwardInformationEvent",
#     "obligated dates": xpath.text_sibling("td", "Obligated dates", 2),
#     "anticipated dates": xpath.text_sibling("td", "Anticipated dates", 2),
#     "dates_dollars direct": "xpath=//td[contains(text(), 'Obligated ($.00)')]/ancestor::table[1]//tr[@class='bg0'][position()=5]",
#     "dates_dollars indirect" : "xpath=//td[contains(text(), 'Obligated ($.00)')]/ancestor::table[1]//tr[@class='bg0'][position()=6]",
#     "dates_dollars total": "xpath=//td[contains(text(), 'Obligated ($.00)')]/ancestor::table[1]//tr[@class='bg0'][position()=7]",
#     "new segment home": "xpath=//a[contains(@href, '/gmas/project/SCR0104SegmentHome')]",
#     "nickname": "xpath=//td[@id='nickNameValue']",
#     "title": xpath.text_sibling("td", "Title", 2),
#     "pi": xpath.text_sibling("td", "Principal Investigator", 1),
#     "sponsor": xpath.text_sibling("td", "Sponsor", 1),
#     "fund": xpath.text_sibling("td", "Fund", 2),
#     "status": xpath.text_sibling("td", "Project Information", 2),
#     "mentor": xpath.text_sibling("td", "Mentor Investigator", 1),
#     "prime sponsor": xpath.text_sibling("td", "Prime sponsor", 1),
#     "project": xpath.text_sibling("td", "Project Information", 2),
#     "open all": "link=open all",
#     "budget dates": xpath.text_sibling("td", "Budget", 2),
#     "budget direct": "xpath=//span[contains(normalize-space(text()), 'Total')]/../following-sibling::td[4]",
#     "budget indirect": "xpath=//span[contains(normalize-space(text()), 'Total')]/../following-sibling::td[8]",
#     "budget total": "xpath=//span[contains(normalize-space(text()), 'Total')]/../following-sibling::td[12]"
       }

    _locators = {
    "more details": "link=More details...",        
    "project_id": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr/td[2]",
    "tub":"xpath=//table[@id='segmentSummaryGrid']/tbody/tr[2]/td[2]/a",
    "org": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr[3]/td[2]/a",
    "nickname": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr[4]/td[2]",
    "project type": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr[5]/td[2]",
    "AARA funding": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr[6]/td[2]",
    "uniform guidance": "xapth=//table[@id='segmentSummaryGrid']/tbody/tr[7]/td[2]",
    "agency fund": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr[8]/td[2]",
    "plan 294": "xpath=//table[@id='segmentSummaryGrid']/tbody/tr[9]/td[2]",
    "sponsor type": "xpath=//span[contains(normalize-space(text()), 'Sponsor type')]/../following-sibling::td[1]",
    "prime sponsor type": "xpath=//span[contains(normalize-space(text()), 'Prime sponsor type')]/../following-sibling::td[1]",
    "prime PI": "xpath=//span[contains(normalize-space(text()), 'Prime Institute PI')]/../following-sibling::td[1]",
    "award number": "xpath=//span[contains(normalize-space(text()), 'Award number')]/../following-sibling::td[1]",
    "prime award number": "xpath=//span[contains(normalize-space(text()), 'Prime award number')]/../following-sibling::td[1]",
    "funding instrument": "xpath=//span[contains(normalize-space(text()), 'Funding instrument')]/../following-sibling::td[1]",
    "CFDA number": "xpath=//span[contains(normalize-space(text()), 'CFDA number')]/../following-sibling::td[1]",
    "discipline": "xpath=//span[contains(normalize-space(text()), 'Discipline')]/../following-sibling::td[1]",
    "payment method": "xpath=//span[contains(normalize-space(text()), 'Payment method')]/../following-sibling::td[1]",
    "agency LOC number": "xpath=//span[contains(normalize-space(text()), 'Agency LOC number')]/../following-sibling::td[1]"
#     "obligated dates": "xpath=//table[@id='segmentDatesGrid']/tbody/tr/td[2]",
#     "anticipated dates": "xpath=//table[@id='segmentDatesGrid']/tbody/tr[2]/td[2]",
#     "dates_dollars direct": "xpath=//table[@id='segmentDollarsGrid']/tbody/tr[2]",
#     "dates_dollars indirect" : "xpath=//table[@id='segmentDollarsGrid']/tbody/tr[3]",
#     "dates_dollars total": "xpath=//table[@id='segmentDollarsGrid']/tbody/tr",
#     "nickname": "css=span.nickname",
#     "title": "css=span.name",
#     "pi": "xpath=//span[@id='projectSnapshotPI']",
#     "sponsor": "xpath=//span[@id='projectSnapshotSponsor']",
#     "fund": "xpath=//span[@id='projectSnapshotFund']",
#     "status": "css=span.project-status",
#     "mentor": "xpath=//span[@id='projectSnapshotMentor']",
#     "prime sponsor": "xpath=//span[@id='projectSnapshotPrimeSponsor']",
#     "project": "xpath=//span[@id='projectInfoProject']"
#     "budget dates": "xpath=//table[@id='proposedSegmentDatesGrid']/tbody/tr/td[2]",
#     "budget direct": "xpath=//table[@id='proposedSegmentDollarsGrid']/tbody/tr/td[2]",
#     "budget indirect": "xpath=//table[@id='proposedSegmentDollarsGrid']/tbody/tr[2]/td[2]",
#     "budget total": "xpath=//table[@id='proposedSegmentDollarsGrid']/tbody/tr[3]/td[2]"
       }
      
      
      
#     obligated_dates = RText("obligated dates", "Obligated dates")
#     anticipated_dates = RText("anticipated dates", "Anticipated dates")
#     nickname = RText("nickname", "Project Nickname")
#     title = RText("title", "Project Title")
#     pi = RText("pi", "Principal investigator")
#     sponsor = RText("sponsor", "Project sponsor")
#     fund = RText("fund", "Fund")
#     status = RText("status", "Status")
#     mentor = RText("mentor", "Mentor")
#     prime_sponsor = RText("prime sponsor", "prime sponsor")
#     project = RText("project", "Project ID")
#     budget_dates = RText("budget dates", "Budget dates")
#     budget_direct = RText("budget direct", "Budget direct")
#     budget_indirect = RText("budget indirect", "Budget indirect")
#     budget_total = RText("budget total", "Budget total")

    tub = RText("tub", "Tub")
    org = RText("org", "Org")
    nickname = RText("nickname", "Nickname")
    project_type = RText("project type", "Project Type")
    AARA_funding = RText("AARA funding", "ARRA (Stimulus) funding?" )
    funding_instrument = RText("funding instrument", "Funding Instrument")
    award_number = RText("award number", "Award number")
    sponsor_type = RText("sponsor type", "Sponsor type")
    prime_sponsortype = RText("prime sponsor type", "Prime sponsor type")
    prime_pi = RText("prime PI", "Prime PI")
    
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
            return self.go("more details")
        except:
            self.find("open all").click()
            return self
#     @property
#     def open_all(self):
#         return self.go("open all")
#     
#     @property
#     def more_details(self):
#       return self.go("more details") 
  
  
#     @property
#     def segment_home(self):
#         if self.mode == "old":
#             return self.go("open all")
#         if self.mode == "convert":
#             return self.go("more details")
          
        
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
        return url.format(segment_id, project_id)
    

#     @classmethod
#     def url(cls, request_id, segment_id):
#         """
#         Direct navigation to segmenthome
#         """
#         url = "{{}}/gmas/dispatch?ref=%2Frequest%2FSCR0344RequestList.jsp&requestTypeId=5003&requestId={}&segmentId={}&formName=RequestListForm&RequestListLinkEvent=&submit"
#         return url.format( request_id, segment_id)
    

            
    
#     @property
#     def nickname(self):
#         if self.mode == "old":
#             text = self.find("nickname").text
#             return text
#         if self.mode == "convert":
#             text = self.find("nickname").text
#             return text[:-1]
#          
#     @property
#     def status(self):
#         if self.mode == "old":
#             text = self.find("status").text
#             return text[26:]
#         if self.mode == "convert":
#             return self.find("status").text
#       
    @property
    def project(self):
        if self.mode == "old":
            text = self.find("project_id").text
            return text[13:23]
        if self.mode == "convert":
            return self.find("project_id").text

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

#     @property
#     def status(self):
#         """
#         status  
#         """
#         if self.mode == "old" :
#             return self.find("status").text.split()[:6]
#         if self.mode == "convert":
#             return self.find("status")
#   
# 
#         
# 
#     def continue_revision(self):
#         """
#         Clicks the "continue making changes" link for an open revision
#         Goes to SCR_0105
#         """
#         self.find("continue revision").click()
#         return self.load_page()
# 
#     def confirm_research_team(self):
#         """
#         Clicks the <Confirm research team> button
#         Goes to SCR_0645
#         """
#         return self.go("confirm research team")
# 
#     def goto_documents(self):
#         """
#         Clicks the "Documents" link
#         Goes to SCR_0433
#         """
#         return self.go("documents")
# 
#     def goto_dates_dollars(self):
#         """
#         Clicks the "Dates and Dollars" link
#         Goes to SCR_0070
#         """
#         return self.go("dates_dollars")
# 
#     def goto_additional_info(self):
#         """
#         Clicks the "Additional award information" link
#         Goes to SCR_0519
#         """
#         return self.go("additional info")
# 
#     def goto_approvals(self):
#         """
#         Clicks the "Approvals" link
#         Goes to SCR_0080
#         """
#         return self.go("approvals")
# 
#     def goto_notices(self):
#         """
#         Clicks the "Sponsor notices" link
#         Goes to SCR_0308
#         """
#         return self.go("notices")
# 
#     def goto_subagreements(self):
#         """
#         Clicks the "Subagreements" link
#         Goes to SCR_0232
#         """
#         return self.go("subagreements")
# 
#     def goto_research_team(self):
#         """
#         Clicks the "Research staff" link
#         Goes to SCR_0015
#         """
#         return self.go("research team")
# 
#     def goto_admin_team(self):
#         """
#         Clicks the "Administrative team" link
#         Goes to SCR_0300
#         """
#         return self.go("admin team")
# 
#     def goto_requests(self):
#         """
#         Clicks the "Requests" link
#         Goes to SCR_0344
#         """
#         return self.go("requests")
# 
#     def goto_accounts(self):
#         """
#         Clicks the "Accounts" link
#         Goes to SCR_0360
#         """
#         return self.go("accounts")
# 
#     def goto_segment_documents(self):
#         """
#         Clicks the "Segment documents" link
#         Goes to SCR_0634
#         """
#         return self.go("segment documents")
# 
#     def goto_revisions(self):
#         """
#         Clicks the "Revisions" link
#         Goes to SCR_0425
#         """
#         return self.go("revisions")
# 
#     def goto_event_history(self):
#         """
#         Clicks the "Event history" link
#         Goes to SCR_0002
#         """
#         return self.go("event history")
# 
#     def goto_todos(self):
#         """
#         Clicks the "Segment to-do's" link
#         Goes to SCR_0159
#         """
#         return self.go("todos")
     
#     def open_all(self):
#         """
#         Click the open all 
#         """
#         self.find("open all").click()
#         
#     @property
#     def new_segment(self):
#         """
#         Click the new segment home link 
#         """
#         return self.go("new segment home")
    

#     def goto_financial_award_info(self):
#         """
#         Clicks the "Financial award information" link
#         Goes to SCR_0647
#         """
#         return self.go("fin award info")
    
#     @property
#     def dates_dollars_direct(self):
#         """
#         List of all rows from the "dates and dollars" table
#         """
#         return [self.Dates_dollars_direct(row, self) for row in self.finds("dates_dollars direct")]
#     
#     class Dates_dollars_direct(Row):
#         locators = {
#             "type": Row.cell(2),
#             "obligated": Row.cell(6),
#             "anticipated": Row.cell(10),
#             "expenses": Row.cell(14),
#             "balance": Row.cell(18)
#         }
#         
#         _locators = {
#             "type": Row.cell(1),
#             "obligated": Row.cell(2),
#             "anticipated": Row.cell(3),
#             "expenses": Row.cell(4),
#             "balance": Row.cell(5)
#         }
#         
#         type = RText("type", "Type")
#         obligated = RText("obligated", "Obligated")
#         anticipated = RText("anticipated", "Anticipated")
#         expenses = RText("expenses", "Expenses")
#         balance = RText("balance", "Balance")
#         
#     @property
#     def dates_dollars_indirect(self):
#         """
#         List of all rows from the "dates and dollars" table
#         """
#         return [self.Dates_dollars_indirect(row, self) for row in self.finds("dates_dollars indirect")]
#     
#     class Dates_dollars_indirect(Row):
#         locators = {
#             "type": Row.cell(2),
#             "obligated": Row.cell(6),
#             "anticipated": Row.cell(10),
#             "expenses": Row.cell(14),
#             "balance": Row.cell(18)
#         }
#         
#         _locators = {
#             "type": Row.cell(1),
#             "obligated": Row.cell(2),
#             "anticipated": Row.cell(3),
#             "expenses": Row.cell(4),
#             "balance": Row.cell(5)
#         }
#         
#         type = RText("type", "Type")
#         obligated = RText("obligated", "Obligated")
#         anticipated = RText("anticipated", "Anticipated")
#         expenses = RText("expenses", "Expenses")
#         balance = RText("balance", "Balance")
#         
#     @property
#     def dates_dollars_total(self):
#         """
#         List of all rows from the "dates and dollars" table
#         """
#         return [self.Dates_dollars_total(row, self) for row in self.finds("dates_dollars total")]
#     
#     class Dates_dollars_total(Row):
#         locators = {
#             "type": Row.cell(2),
#             "obligated": Row.cell(6),
#             "anticipated": Row.cell(10),
#             "expenses": Row.cell(14),
#             "balance": Row.cell(18)
#         }
#         
#         _locators = {
#             "type": Row.cell(1),
#             "obligated": Row.cell(2),
#             "anticipated": Row.cell(3),
#             "expenses": Row.cell(4),
#             "balance": Row.cell(5)
#         }
#         
#         type = RText("type", "Type")
#         obligated = RText("obligated", "Obligated")
#         anticipated = RText("anticipated", "Anticipated")
#         expenses = RText("expenses", "Expenses")
#         balance = RText("balance", "Balance")