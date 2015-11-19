from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0426(Page):
    """
    SCR_0426 Segment revision detail
    """
    locators = {
        "open_all": "link=open all",
        "revision attributes": "xpath=//td[contains(text(), 'Revision attributes')]/ancestor::tr[1]/following-sibling::tr[3]",
        "date initiated": "xpath=//span[contains(normalize-space(text()), 'Date initiated')]/../following-sibling::td[2]",
        "date committed": "xpath=//span[contains(normalize-space(text()), 'Date committed')]/../following-sibling::td[2]",
        "revision id":"xpath=//span[contains(normalize-space(text()), 'Revision Id')]/../following-sibling::td[2]",
        "created by": xpath.text_sibling("td", "Created by", 2),
        "committed by": xpath.text_sibling("td", "Committed by", 2),
        "type": xpath.text_sibling("td", "Type", 2),
        "status": xpath.text_sibling("td", "Status", 2),
        "notification recipients": "xpath=//td[contains(text(), 'Name')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>1]",
        "associated notice information":"xpath=//td[contains(text(), 'Revise the segment based on a sponsor notice')]",
        "sponsor legal title": xpath.text_sibling("td", "Sponsor legal title", 2),
        "sponsor award no": xpath.text_sibling("td", "Sponsor award no.", 2),
        "amendment no": xpath.text_sibling("td", "Amendment no.", 2),
        "form of notice": xpath.text_sibling("td", "Form of notice", 2),
        "date issued": "xpath=//span[contains(normalize-space(text()), 'Date issued')]/../following-sibling::td[2]",
        "date received by harvard": xpath.text_sibling("td", "Date received by Harvard", 2),
        "date fully executed": xpath.text_sibling("td", "Date fully executed", 2),
        "action memo comments": "xpath=//*[contains(normalize-space(text()), 'Revision comments')]/ancestor::tr[1]/following-sibling::tr[4]",
        "correction information": "xpath=//*[contains(normalize-space(text()), 'Reason for administrative change or correction')]/ancestor::tr[1]/following-sibling::tr[3]",
        "associated internal request": "xpath=//td[contains(text(), 'Revise the segment based on an internal request')]",
        "request title": "xpath=//span[contains(normalize-space(text()), 'Request title')]/../following-sibling::td[2]",
        "request type": xpath.text_sibling("td", "Request type", 2),
        "date submitted to central": xpath.text_sibling("td", "Date submitted to central", 2),
        "Award identifying row": "xpath=//td[contains(text(), 'Award identifying information')]/following::table[1]//tr[not (@class ='bg3')][position()  mod 2 =1 and position()>2]",
        "sponsor_row": "xpath=//td[contains(text(), 'Sponsors')]/following::table[1]//tr[not (@class ='bg3')][position()  mod 2 =1 and position()>2]",
        "awarded_row": "xpath=//td[contains(text(), 'Budget period (mm-dd-yyyy)')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>2 and position()<last()]",
        "total_row": "xpath=//td[contains(text(), 'Budget period (mm-dd-yyyy)')]/ancestor::table[1]//tr[not (@class ='bg3')][last()]",
        "subagreements_row": "xpath=//td[contains(text(), 'Subagreements')]/ancestor::table[1]//tr[not (@class ='bg1')][position()  mod 2 =1 and position()>3]",
        "total fund authorized to pending subagreements": xpath.text_sibling_child("td", "Total funds authorized to pending subagreements", 2),
        "estimated Harvard University overhead for subagreements": xpath.text_sibling_child("td", "Estimated Harvard University overhead for subagreements", 2),
        "allocation_row": "xpath=//td[contains(text(), 'Grp.')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>1]",
        "account_row": "xpath=//td[contains(text(), 'Description')]/ancestor::table[1]//tr[(@class ='bg0')][position()>1]",
        "costsharing_row": "xpath=//td[contains(text(), 'Mandatory')]/ancestor::table[1]//tr[not (@class ='bg3')][position()  mod 2 =1 and position()>1]",
        "approvalattributes_row": "xpath=//td[contains(text(), 'Approval attributes')]/following::table[1]//tr[not (@class ='bg3')][position()  mod 2 =1 and position()>2]"
        }


    
    _locators = {
        "open_all": "link=Open all",
        "date initiated": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr/td[2]",
        "date committed": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr[2]/td[2]",
        "revision id": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr[3]/td[2]",
        "created by": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr[4]/td[2]",
        "committed by": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr[5]/td[2]",
        "type": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr[6]/td[2]",
        "status": "xpath=//table[@id='actionMemoAttributesGrid']/tbody/tr[7]/td[2]",
        "notification recipients": "css=[id$=notificationRecipientsGrid] tbody tr",
        "associated notice information": "link=Associated notice information",
        "sponsor legal title": "xpath=//span[contains(normalize-space(text()), 'Sponsor legal title')]/../following-sibling::td[1]",
        "sponsor award no": "xpath=//span[contains(normalize-space(text()), 'Sponsor award no.')]/../following-sibling::td[1]",
        "amendment no": "xpath=//span[contains(normalize-space(text()), 'Amendment no.')]/../following-sibling::td[1]",
        "form of notice": "xpath=//span[contains(normalize-space(text()), 'Form of notice')]/../following-sibling::td[1]",
        "date issued": "xpath=//span[contains(normalize-space(text()), 'Date issued')]/../following-sibling::td[1]",
        "date received by harvard": "xpath=//span[contains(normalize-space(text()), 'Date received by Harvard')]/../following-sibling::td[1]",
        "date fully executed": "xpath=//span[contains(normalize-space(text()), 'Date fully executed')]/../following-sibling::td[1]",
        "action memo comments": "xpath=//table[@id='actionMemoCommentsGrid']/tbody/tr/td",
        "correction information": "xpath=//table[@id='administrativeChangeInformationGrid']/tbody/tr/td",
        "correction information": "xpath=//*[contains(normalize-space(text()), 'Reason for administrative change or correction')]/ancestor::tr[1]/following-sibling::tr[3]",
        "associated internal request": "link=Associated internal request information",
        "request title": "xpath=//span[contains(normalize-space(text()), 'Request title')]/../following-sibling::td[1]",
        "request type": "xpath=//span[contains(normalize-space(text()), 'Request type')]/../following-sibling::td[1]",
        "date submitted to central": "xpath=//span[contains(normalize-space(text()), 'Date submitted to central')]/../following-sibling::td[1]",
        "Award identifying row": "css=[id$=awardIdentifyingInformationPanel_content] tbody tr",
        "sponsor_row": "css=[id$=sponsorPanel_content] tbody tr",
        "awarded_row": "xpath=//*[(@id ='awardedDatesDollarsDatatable_data')]//tr[not (@class ='bg3')][position()>0]",
        "total_row": "xpath=//*[(@id ='awardedDatesDollarsDatatable_foot')]//tr[not (@class ='bg3')][position()>0]",
        "subagreements_row": "css=[id$=subagreement_content_content] tbody tr",
        "total fund authorized to pending subagreements": "xpath=//span[contains(normalize-space(text()), 'Total funds authorized to pending subagreements')]/../following-sibling::td[1]",
        "estimated Harvard University overhead for subagreements": "xpath=//span[contains(normalize-space(text()), 'Estimated Harvard University overhead for subagreements')]/../following-sibling::td[1]",
        "allocation_row": "css=[id$=allocation_content_content] tbody tr",
        "account_row": "css=[id$=accounts_content_content] tbody tr",
        "costsharing_row": "css=[id$=costSharing_content_content] tbody tr",
        "approvalattributes_row": "css=[id$=j_idt351_content] tbody tr"
    }
         

          
                 
                 
                 
                 
    @classmethod
    def url(cls, segment_id, revision_id):
        """
        Direct navigation to SCR_0426
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Frevision%2FSCR0425RevisionsList.jsp&segmentId={}&formName=ListOfRevisionsForm&noBusinessLock=true&segmentRevisionId={}&ListOfRevisionsAppliedRevisionDetailEvent=&submit"
        return url.format(segment_id, revision_id)
    
    
    
#     date_initiated = RText("date initiated", "Date initiated")
#     date_committed = RText("date committed", "Date committed")
#     revision_id = RText("revision id", "Revision id")
#     created_by = RText("created by", "Created by")
#     committed_by = RText("committed by", "Committed by")
#     type = RText("type", "Type")
#     status = RText("status", "Status")
#     notification_recipients = RText("notification recipients", "Notification recipients")
#     actionmemo_comments = RText("action memo comments", "Action memo comments")
#     request_title = RText("request title", "Request title")
#     request_type = RText("request type", "Request type")
#     date_central = RText("date submitted to central", "Date submitted to central")
#     sponsor_title = RText("sponsor legal title", "Sponsor legal title")
#     sponsor_award = RText("sponsor award no", "Sponsor award no")
#     form_notice = RText("form of notice", "Form of notice")
#     date_issued = RText("date issued", "Date issued")
#     date_received = RText("date received by harvard", "Date received by harvard")
#     date_executed = RText("date fully executed", "Date fully executed")
#     amendment_no = RText("amendment no", "Amendment no")
#     reason = RText("reason", "Reason")
#     sponsors = RText("sponsors", "Sponsors")
#     allocation_awardedfunds = RText("allocation of awarded funds to accounts", "Allocation of awarded funds to accounts")
#     accounts = RText("accounts", "Accounts")
#     cost_sharing = RText("cost sharing", "Cost sharing")
#     approval_attributes =  RText("approval attributes", "Approval attributes")
#     total_fund  = RText("total fund authorized to pending subagreements", "Total fund authorized to pending subagreements")
#     estimated_Harvard  = RText("estimated Harvard University overhead for subagreements", "Estimated Harvard University overhead for subagreements")
#     
    
    @property
    def approvalattributes_row(self):
        """
        List of all rows from the "approval attributes" table
        """
        return [self.Approvalattributes_row(row, self) for row in self.finds("approvalattributes_row")]

    @property
    def notification_recipients(self):
        """
        List of all rows from the "Notification recipients" table
        """
        return [self.Notification_recipients(row, self) for row in self.finds("notification recipients")] 
     
    class Notification_recipients(Row): 
        locators = {
            "name": Row.cell(1),
            "role": Row.cell(3)
        }  
     
        _locators = {
            "name": Row.cell(1),
            "role": Row.cell(2)                   
        }
         
        name = RText("name", "Name")
        role = RText("role", "Role")

    def open_all(self):
        """
        Click "open all"
        """
        return self.go("open_all")
     
    @property
    def award_identifying(self):
        """
        List of all rows from the "Award identifying informations" table
        """
        return [self.Award_identifying(row, self) for row in self.finds("Award identifying row")]
      
    @property
    def award_row(self):
        """
        List of all rows from the "Award dates and dollars" table
        """
        return [self.Awarded_row(row, self) for row in self.finds("awarded_row")]
      
    @property
    def total_row(self):
        """
        List of all rows from the "total dates and dollars" table
        """
        return [self.Total_row(row, self) for row in self.finds("total_row")]
 
 
      
    @property
    def alloacation_row(self):
        """
        List of all rows from the "Allocation of awarded funds to accounts" table
        """
        return [self.Allocation_row(row, self) for row in self.finds("allocation_row")]
      
    @property
    def subagreements_row(self):
        """
        List of all rows from the "Subagreements" table
        """
        return [self.Subagreements_row(row, self) for row in self.finds("subagreements_row")]
     
    @property
    def account_row(self):
        """
        List of all rows from the "Subagreementss" table
        """
        return [self.Account_row(row, self) for row in self.finds("account_row")]
     
    @property
    def sponsor_row(self):
        """
        List of all rows from the "Sponsors" table
        """
        return [self.Sponsor_row(row, self) for row in self.finds("sponsor_row")]
#     
    @property
    def costsharing_row(self):
        """
        List of all rows from the "cost sharing" table
        """
        return [self.Costsharing_row(row, self) for row in self.finds("costsharing_row")]
    
    
    class Award_identifying(Row):
        locators = {
            "feild or value": Row.cell(2),
            "previous value": Row.cell(6),
            "new value": Row.cell(10)
        }
         
        _locators = {
            "feild or value": Row.cell(1),
            "previous value": Row.cell(2),
            "new value": Row.cell(3)
        }
          
        feild_value = RText("feild or value", "Feild or value")
        previous_value = RText("previous value", "Previous value")
        new_value = RText("new value", "New value")


    class Awarded_row(Row):
        locators = {
            "budget": Row.cell(2),
            "obligated_current": Row.cell(6),
            "obligated_change": Row.cell(10),
            "obligated_total": Row.cell(14),
            "anticipated_current": Row.cell(18),
            "anticipated_change": Row.cell(22),
            "anticipated_total": Row.cell(26),
            "carried forward_current": Row.cell(30),
            "carried forward_change": Row.cell(34),
            "carried forward_total": Row.cell(38)
        }
             
        _locators = {
            "budget": Row.cell(1),
            "obligated_current": Row.cell(2),
            "obligated_change": Row.cell(3),
            "obligated_total": Row.cell(4),
            "anticipated_current": Row.cell(5),
            "anticipated_change": Row.cell(6),
            "anticipated_total": Row.cell(7),
            "carried forward_current": Row.cell(8),
            "carried forward_change": Row.cell(9),
            "carried forward_total": Row.cell(10)
        }
         
        budget = RText("budget", "Budget  period")
        obligated_current = RText("obligated_current", "obligated_current")
        obligated_change = RText("obligated_total","obligated_total")
        obligated_total = RText("obligated_total", "obligated_total")
        anticipated_current = RText("anticipated_current", "anticipated_current")
        anticipated_change = RText("anticipated_change", "anticipated_change")
        anticipated_total = RText("anticipated_total", "anticipated_total")
        carriedforward_current = RText("carried forward_current","carried forward_current")
        carriedforward_change = RText("carried forward_change", "carried forward_change")
        carriedforward_total = RText("carried forward_total", "carried forward_total")
         
    class Total_row(Row):
        locators = {
            "budget": Row.cell(2),
            "obligated_current": Row.cell(6),
            "obligated_change": Row.cell(10),
            "obligated_total": Row.cell(14),
            "anticipated_current": Row.cell(18),
            "anticipated_change": Row.cell(22),
            "anticipated_total": Row.cell(26),
            "carried forward_current": Row.cell(30),
            "carried forward_change": Row.cell(34),
            "carried forward_total": Row.cell(38)
        }
             
        _locators = {
            "budget": Row.cell(1),
            "obligated_current": Row.cell(2),
            "obligated_change": Row.cell(3),
            "obligated_total": Row.cell(4),
            "anticipated_current": Row.cell(5),
            "anticipated_change": Row.cell(6),
            "anticipated_total": Row.cell(7),
            "carried forward_current": Row.cell(8),
            "carried forward_change": Row.cell(9),
            "carried forward_total": Row.cell(10)
        }
         
        budget = RText("budget", "Budget  period")
        obligated_current = RText("obligated_current", "obligated_current")
        obligated_change = RText("obligated_total","obligated_total")
        obligated_total = RText("obligated_total", "obligated_total")
        anticipated_current = RText("anticipated_current", "anticipated_current")
        anticipated_change = RText("anticipated_change", "anticipated_change")
        anticipated_total = RText("anticipated_total", "anticipated_total")
        carriedforward_current = RText("carried forward_current","carried forward_current")
        carriedforward_change = RText("carried forward_change", "carried forward_change")
        carriedforward_total = RText("carried forward_total", "carried forward_total")



        

    class Allocation_row(Row):
        locators = {
            "grp": Row.cell(2),
            "account(s)": Row.cell(6),
            "type": Row.cell(10),
            "description": Row.cell(14),
            "current": Row.cell(18),
            "change": Row.cell(22),
            "total": Row.cell(26)
        } 
        
        _locators = {
            "grp": Row.cell(1),
            "account(s)": Row.cell(2),
            "type": Row.cell(3),
            "description": Row.cell(4),
            "current": Row.cell(5),
            "change": Row.cell(6),
            "total": Row.cell(7)
        } 
        grp = RText("grp", "Grp")
        account = RText("account(s)", "Accounts(s)")
        type = RText("type", "Type")
        description = RText("description", "Description")
        current = RText("current", "Current($.00)")
        change = RText("change", "Change($.00)")
        total = RText("total", "Total($.00)")
#         
    class Subagreements_row(Row):
        locators = {
            "subrecipient": Row.cell(2),
            "authorized, non-issued funds": Row.cell(6),
            "estimated HU overhead": Row.cell(10)    
        }
        
        _locators = {
            "subrecipient": Row.cell(1),
            "authorized, non-issued funds": Row.cell(2),
            "estimated HU overhead": Row.cell(3)    
        }
        
        subrecipient = RText("subrecipient", "Subrecipient")
        authorized_funds = RText("authorized, non-issued funds", "Authorized, non-issued funds")
        estimated_overhead = RText("estimated HU overhead", "Estimated HU overhead")
         
    class Account_row(Row):
        locators = {
            "grp": Row.cell(2),
            "description": Row.cell(6),
            "year": Row.cell(10),
            "type": Row.cell(14),
            "tub": Row.cell(18),
            "auth": Row.cell(22),
            "fund": Row.cell(26),
            "activity": Row.cell(30),
            "sub activity": Row.cell(34),
            "auth.root": Row.cell(38),
            "at risk": Row.cell(42),
            "type of revision": Row.cell(46)
                     
        }
        
        _locators = {
            "grp": Row.cell(1),
            "description": Row.cell(2),
            "year": Row.cell(3),
            "type": Row.cell(4),
            "tub": Row.cell(5),
            "auth": Row.cell(6),
            "fund": Row.cell(7),
            "activity": Row.cell(8),
            "sub activity": Row.cell(9),
            "auth.root": Row.cell(10),
            "at risk": Row.cell(11),
            "type of revision": Row.cell(12)
                     
        }
        
        grp = RText("grp", "grp")
        description = RText("description", "description")
        year = RText("year", "year")
        type = RText("type", "type")
        tub = RText("tub", "tub")
        auth = RText("auth", "auth.org")
        fund = RText("fund", "Fund")
        activity = RText("activity", "Activity")
        sub_activity = RText("sub activity", "Sub activity")
        auth_root = RText("auth.root", "Auth.root")
#         at_risk = RText("at risk", "At risk")
        revision_type = RText("type of revision", "Type of revision")
        
        @property
        def at_risk(self):
            """
            verify at-risk is checked
            """
            element = self.find("at risk")
            if self.page.mode == "old":
                # Is there an image in the cell?
                images = element.find_elements_by_tag_name("img")
                if len(images) == 0:
                    return "No"
                else:
                    return "Yes"
                # If yes - return "Yes"
                # If no - return "No"
            elif self.page.mode == "convert":
                return element.text
             
                     
    class Sponsor_row(Row):
        locators = {
            "field or value": Row.cell(2),
            "previous value": Row.cell(6),
            "new value": Row.cell(10)
        }
        
        _locators = {
            "field or value": Row.cell(1),
            "previous value": Row.cell(2),
            "new value": Row.cell(3)
        }
        field_value = RText("field or value", "Field or value")
        previous_value = RText("previous value", "Previous value")
        new_value =  RText("new value", "New value") 
        
             
    class Costsharing_row(Row):
         
        locators = {
            "description": Row.cell(2),
            "mandatory": Row.cell(6),
            "voluntary": Row.cell(10),
            "total": Row.cell(14)     
        }
        
        _locators = {
            "description": Row.cell(1),
            "mandatory": Row.cell(2),
            "voluntary": Row.cell(3),
            "total": Row.cell(4)     
        }
         
        description = RText("description", "Description")
        mandatory = RText("mandatory", "Mandatory")
        voluntary = RText("voluntary", "Voluntary")
        total = RText("total", "Total")
     
    class Approvalattributes_row(Row):
         
        locators = {
            "field or value": Row.cell(2),
            "previous value": Row.cell(6),
            "new value":    Row.cell(10)        
        }
        _locators = {
            "field or value": Row.cell(1),
            "previous value": Row.cell(2),
            "new value":    Row.cell(3)        
        }
             
        feild_value = RText("field or value", "Field or value")
        previous_value = RText("previous value", "Previous value")
        new_value =  RText("new value", "New value")        
         
         
        
        
        
