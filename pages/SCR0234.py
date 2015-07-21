from pages.Page import Page
from pages.elements import Row, RText, Text, Select, Checkbox, Radio 
import utilities.xpath as xpath
import datetime
from gmas_webdriver.utilities import dates

class SCR0234(Page):
    
    """
    New amendment quetsions
    """
    locators = {
        "amendment row": "xpath=//td[contains(text(), 'Fully executed to date')]/ancestor::table[1]//tr[not (@class='bg3')][position()>2]",
        "subagreement type": "css=select[name='subagreementType']",
#         "subagreement type": xpath.text_sibling("td[@class='input']", "Subagreement type", 2),
#         "select if applicable_contacts": "xpath=//input[@name='checkContact']" ,
#         "select if applicable_reports": "xpath=//input[@name='checkReport']",
        "Is this amendment terminating the agreement?": "name=terminateSubagreement",
        "total issued to date": "xpath=//td[contains(text(), 'Total issued to date')]/ancestor::table[1]//tr[@class='bg3'][position()=4]",
#         "total issued to date": "xpath=//td[contains(text(), 'Total issued to date')]/ancestor::table[1]//tr[@class='bg3'][mod 2 = 1 and position()>4]",
        "authorized for subrecipient": "xpath=//td[contains(text(), 'Authorized for Subrecipient')]/ancestor::table[1]//tr[@class='bg3'][position()=6]"
    }
    
    _locators = {
        "amendment row": "xpath=//tbody[@id='createAmendmentForm:amendmentsDatatable_data']/tr",
        "subagreement type": "id=createAmendmentForm:subagreementType_label",
        "Is this amendment terminating the agreement?": "terminatingAgreement",
        "total issued to date":"xpath=//tfoot[@id='createAmendmentForm:amendmentsDatatable_foot']/tr[1]",
        "authorized for subrecipient": "xpath=//tfoot[@id='createAmendmentForm:amendmentsDatatable_foot']/tr[2]"
    }
    
    subagreement_type = RText("subagreement type", "Subagreement type")
#     applicable_contacts = Checkbox("select if applicable_contacts", "Select if applicable_contacts")
#     applicable_reports = Checkbox("select if applicable_reports", "Select if applicable_reports")
    amendment_agreement = Radio ("Is this amendment terminating the agreement?", "Is this amendment terminating the agreement?")
    
    
    @classmethod
    def url(cls, subagreement_Id, segment_Id):
        """
        Direct navigation to SCR_234
        """
        url = "{{}}/gmas/dispatch?ref=%2Fsubagreement%2FSubagreementHomeAmendmentsInclude.jsp&subagreementId={}&segmentId={}&formName=SubagreementHomeForm&CreateAmendmentEvent"
        return url.format(subagreement_Id, segment_Id)
 
    
    
    @property
    def amendments(self):
        """
        Returns the nth amendment in the list
        //Amendment_row
        """
        return [self.Amendment_row(row, self) for row in self.finds("amendment row")]
    
    
    class Amendment_row(Row):
        locators = {
            "executed date": Row.cell(2),
            "sub PI": Row.cell(6),
            "dates": Row.cell(10),
            "dollars": Row.cell(14)
        }
 
        _locators = {
            "executed date": Row.cell(1),
            "sub PI": Row.cell(2),
            "dates": Row.cell(3),
            "dollars": Row.cell(4)
        }   
    
        executed_date = RText("executed date", "Executed date")
        sub_pi = RText("sub PI", "Subrecipient PI")
        dates = RText("dates", "Dates")
        dollars = RText("dollars", "Dollars")
        
        
    @property
    def total_issued(self):
       
        return [self.Total_issued(row, self) for row in self.finds("total issued to date")]
        
    class Total_issued(Row):
        locators = {
            "total issued to date": Row.cell(6),
            "dates": Row.cell(10),
            "dollars": Row.cell(14)       
        }
        _locators = {
            "total issued to date": Row.cell(1),
            "dates": Row.cell(2),
            "dollars": Row.cell(3)       
        }        
        
    
        total_issued = RText("total issued to date", "Total issued to date")
        dates = RText("dates", "Dates")
        dollars = RText("dollars", "Dollars")
        
    @property
    def authorized_row(self):
       
        return [self.Authorized_row(row, self) for row in self.finds("authorized for subrecipient")]
        
    class Authorized_row(Row):
        locators = {
            "authorized for subrecipient": Row.cell(6),
            "dates": Row.cell(10),
            "dollars": Row.cell(14)                    
        }
        _locators = {
            "authorized for subrecipient": Row.cell(1),
            "dates": Row.cell(2),
            "dollars": Row.cell(3)                    
        }

        authorized_subrecipient = RText("authorized for subrecipient", "Authorized for subrecipient")
        dates = RText("dates", "Dates")
        dollars = RText("dollars", "Dollars")
         
        
        
