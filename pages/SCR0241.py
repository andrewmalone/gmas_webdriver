from pages.Page import Page
from pages.elements import Row, RText, Text, Select, Checkbox, Radio 
import utilities.xpath as xpath
import datetime

class SCR0241(Page):
    """
    SCR_0241 Edit amendment
    """
    locators = {
        "subrecipient name": xpath.text_sibling("td", "Subrecipient name", 2),
        "subrecipient PI": "name=vendorPI",
        "description": "name=description",
        "status": "xpath=//td[contains(text(), 'Status')]/following-sibling::td[2]//tr/td[1]",
        "status date": "xpath=//td[contains(text(), 'Status')]/following-sibling::td[2]//tr/td[3]",
        "subagreement number":  xpath.text_sibling("td", "Subagreement number", 2),
        "subagreement type": "name=subagreementType",
        "date sent to subrecipient": "name=dateSentToSubrecipient",
        "Total issued to date": "xpath=//span[contains(text(), 'Dates')]/ancestor::table[1]//tr[not (@class ='bg3')][position() = 4]",
        "authorized for subrecipient": "xpath=//span[contains(text(), 'Dates')]/ancestor::table[1]//tr[not (@class ='bg3')][position() = 6]",
        "Should the start date be the new start date of the overall subagreement?": xpath.text_sibling("td", "Should the start date be the new start date of the overall subagreement?", 2),
        "start date": "name=amendmentStartDate",
        "end date": "name=amendmentEndDate",
        "anticipated end date": "name=anticipatedEndDate",
        "sub amount": "name=amountToBeIssued",
        "sub anticipated": "xpath=//span[contains(normalize-space(text()), 'Subrecipient anticipated')]/../following-sibling::td[2]",
        "sub row": "xpath=//span[contains(text(), 'Subrecipient indirect')]/ancestor::table[1]//tr[not (@class ='bg3')][position()  mod 2 =1 and position()>2]",
        "indirect basis": "name=idcBasis",
        "reporting row": "xpath=//td[contains(text(), 'Reporting requirements')]/ancestor::table[1]//tr[not (@class='bg1')][position()  mod 2 =1 and position()>2]",
        "all that apply": "xpath=//input[@type='checkbox']",
        "add rate": "xpath=//span[contains(text(), 'Subrecipient indirect')]/ancestor::td[1]/following-sibling::td[2]"
        
    }
    _locators = {
        "subrecipient name": "xpath=//span[@id='editAmendmentForm:subrecipientName']",
        "subrecipient PI": "id=editAmendmentForm:subrecipientPrincipalInvestigator_input",
        "description": "id=editAmendmentForm:description",
        "status": "xpath=//span[@id='editAmendmentForm:status']",
        "status date": "xpath=//span[@id='editAmendmentForm:date']",
        "subagreement number":  xpath.text_sibling("td", "Subagreement number", 2),
        "subagreement type": "id=editAmendmentForm:subagreementType_input",
        "date sent to subrecipient": "id=editAmendmentForm:dateSent_input",
        "Total issued to date": "xpath=//table[@id='editAmendmentForm:j_idt126']/tbody/tr",
        "authorized for subrecipient": "xpath=//table[@id='editAmendmentForm:j_idt126']/tbody/tr[2]",
        "Should the start date be the new start date of the overall subagreement?": xpath.text_sibling("td", "Should the start date be the new start date of the overall subagreement?", 2),
        "start date": "id=editAmendmentForm:startDate_input",
        "end date": "id=editAmendmentForm:endDate_input",
        "anticipated end date": "id=editAmendmentForm:anticipatedEndDate_input",
        "sub amount": "id=editAmendmentForm:subrecipientAmountIssued",
        "sub anticipated": "xpath=//span[@id='editAmendmentForm:subrecipientAnticipated']",
        "sub row": "xpath=//tbody[@id='editAmendmentForm:indirectCostRatesDatatable_data']/tr",
        "indirect basis": "id=editAmendmentForm:indirectbasis_input"
    }
    
    
    @classmethod
    def url(cls, segment_id, subagreement_id, amendment_id, request_id, proposed_parent_budget_id):
        """
        Direct navigation to SCR_0241
        """
        url = "{{}}/gmas/dispatch?submitTime=1434747262937&segmentId={}&subagreementId={}&amendmentId={}&requestId={}&budgetId={}&pageName=subagreements&ReviseFullyExecutedAmendmentEvent.x=38&ReviseFullyExecutedAmendmentEvent.y=11&ref=%2Fsubagreement%2FSCR0240ViewAmendment.jsp&formName=AmendmentForm"
        return url.format(segment_id, subagreement_id, amendment_id, request_id, proposed_parent_budget_id)
    
    subrecipient_name = RText("subrecipient name", "Subrecipient name")
    subrecipient_PI = Text("subrecipient PI", "Subrecipient principal investigator")
    description = Text("description", "Description")
    status = RText("status", "Status")
    status_date = RText("status date", "Date")
    subagreement_type = Text("subagreement type", "Subagreement type")
    date_sent = Text("date sent to subrecipient", "Date sent to subrecipient")
    start_date = Text("start date", "Start date")
    end_date = Text("end date", "End date")
    anticipated_enddate = Text("anticipated end date", "Anticipated end date")
    sub_amount = Text("sub amount", "Subrecipient amt. to be issued ($.00)")
    sub_anticipated = RText("sub anticipated", "Subrecipient anticipated")
    indirect_basis = RText("indirect basis", "Indirect basis")
    
    
    @property
    def total_row(self):
        """
        List of the records with amount rows
        """
        return [self.Total_row(row, self) for row in self.finds("Total issued to date")]
    
    class Total_row(Row):
        locators = {
            "value": Row.cell(2),
            "dates": Row.cell(4),
            "dollars": Row.cell(5)    
        }
        
        _locators = {
            "value": Row.cell(1),
            "dates": Row.cell(2),
            "dollars": Row.cell(3)                      
        }
        
        value = RText("value", "Value")
        date = RText("dates", "Dates")
        dollars = RText("dollars", "Dollars")


    @property
    def authorized_row(self):
        """
        List of the records with amount rows
        """
        return [self.Authorized_row(row, self) for row in self.finds("authorized for subrecipient")]
    

    class Authorized_row(Row):
        locators = {
            "value": Row.cell(2),
            "dates": Row.cell(4),
            "dollars": Row.cell(5)    
        }
        
        _locators = {
            "value": Row.cell(1),
            "dates": Row.cell(2),
            "dollars": Row.cell(3)                      
        }
            
        value = RText("value", "Value")
        date = RText("dates", "Dates")
        dollars = RText("dollars", "Dollars")


    @property
    def sub_row(self):
        """
        List of the records with amount rows
        """
        rows = [self.Sub_row(row, self) for row in self.finds("sub row")]
        if self.mode == "old":
            return rows[:-1]
        if self.mode == "convert":
            return rows
    

    class Sub_row(Row):
        locators = {
            "sub indirect": Row.cell(2) + " input",
            "exp date": Row.cell(3) + " input"
        }
        
        _locators = {
            "sub indirect": Row.cell(1) + " input",
            "exp date": Row.cell(2) + " input"
        }
        
        sub_indirect = Text("sub indirect", "Subrecipient indirect")
        exp_date = Text("exp date", "Expiration date")
        

       

        
