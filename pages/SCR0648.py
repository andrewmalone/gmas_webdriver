from pages.Page import Page
from pages.elements import Row, RText, Select, Text, Checkbox, Radio
import utilities.xpath as xpath


class SCR0648(Page):
    """
    SCR_0648 Edit financial award info
    """
    locators = {
        "contact search": "xpath=//input[@id='finacicalContactForm:contName_input']",
        "salutation": "id=finacicalContactForm:salutation",
        "first name": "id=finacicalContactForm:fName",
        "middle name": "id=finacicalContactForm:mlName",
        "last name": "id=finacicalContactForm:lName",
        "suffix": "id=finacicalContactForm:suffix",
        "address": "id=finacicalContactForm:contactAddress",
        "phone number": "id=finacicalContactForm:phoneNumber",
        "fax number": "id=finacicalContactForm:faxNumber",
        "reporting email": "id=finacicalContactForm:repEmail",
        "contact email": "id=finacicalContactForm:contEmail",
        "PO number": "xpath=//table[@id='finacicalContactForm:rfInfoMgmtQuestionId']/tbody/tr/td/table/tbody/tr[2]/td[4]/input",
        "refund of balances required": "id=finacicalContactForm:rfInfoMgmtQuestionId:1:chooseCarColorid",
        "report submission method": "id=finacicalContactForm:rfInfoMgmtQuestionId:2:chooseCarColorid",
        "report submission comments": "xpath=//table[@id='finacicalContactForm:rfInfoMgmtQuestionId:2:childRfInfoMgmtQuestion']/tbody/tr[3]/td/table/tbody/tr/td[2]",
        "sponsor's approval required for carryfoward": "id=finacicalContactForm:rfInfoMgmtQuestionId:3:chooseCarColorid",
        "deliverable schedule": "id=finacicalContactForm:rfInfoMgmtQuestionId:4:chooseCarColorid",
        "deliverable must be met before billing": "id=finacicalContactForm:rfInfoMgmtQuestionId:4:childRfInfoMgmtQuestionId:0:chooseCarColorid",
        "deliverable must be met before payment is issued": "id=finacicalContactForm:rfInfoMgmtQuestionId:4:childRfInfoMgmtQuestionId:1:chooseCarColorid",
        "deliverable schedule comment": "xpath=//table[@id='finacicalContactForm:rfInfoMgmtQuestionId:4:childRfInfoMgmtQuestionId']/tbody/tr[3]/td/table/tbody/tr/td/textarea",
        "reportable cost share": "id=finacicalContactForm:rfInfoMgmtQuestionId:5:chooseCarColorid1",
        "budget restrictions": "id=finacicalContactForm:rfInfoMgmtQuestionId:6:chooseCarColorid",
        "sponsor withholds a retention": "id=finacicalContactForm:rfInfoMgmtQuestionId:7:chooseCarColorid",
        "Edit_all": "xpath=//input[@name='projectForm:j_idt168']"
    }
    
    _locators = {
        "Edit_all": "css=[id$='editButton']",
        "contact search": "css=[id='editFinancialAwardInfoForm:financialContact_input']",
        "salutation": "id=editFinancialAwardInfoForm:contactSalutation_label",
        "first name": "css=[id='editFinancialAwardInfoForm:contactFirstName']",
        "middle name": "css=[id='editFinancialAwardInfoForm:contactMiddleName']",
        "last name": "css=[id='editFinancialAwardInfoForm:contactLastName']",
        "suffix": "css=[id='editFinancialAwardInfoForm:contactSuffix_label']",
        "address": "id=editFinancialAwardInfoForm:contactAddress_label",
        "phone number": "css=[id='editFinancialAwardInfoForm:contactPhone']",
        "fax number": "id=editFinancialAwardInfoForm:contactFax",
        "reporting email": "css=[id='editFinancialAwardInfoForm:contactReportingEmail']",
        "contact email": "css=[id='editFinancialAwardInfoForm:contactContactEmail']",
        "contact search": "xpath=//input[@id='editFinancialAwardInfoForm:contName_input']",
        "PO number": "css=[id='editFinancialAwardInfoForm:poNumber']",
        "refund of balances required": "css=[id='editFinancialAwardInfoForm:refundOfBalancesRequired']",
        "report submission method": "css=[id='editFinancialAwardInfoForm:reportSubmissionMethod']", 
        "report submission comments": "id=editFinancialAwardInfoForm:electronicSubmissionMethodDropdown_label",
        "sponsor's approval required for carryfoward": "css=[name='ui-radiobutton-icon']",
        "deliverable schedule": "css=[id='editFinancialAwardInfoForm:deliverableSchedulePanel']",
        "deliverable must be met before billing": "css=[id='editFinancialAwardInfoForm:deliverableScheduleMetBillingLabel']",
        "deliverable must be met before payment is issued": "css=[id=editFinancialAwardInfoForm:deliverableScheduleMetPaymentLabel]",
        "deliverable schedule comments": "id=editFinancialAwardInfoForm:deliverableScheduleComments",
        "reportable cost share": "reportableCostShare",
        "budget restrictions": "id=editFinancialAwardInfoForm:budgetRestrictions",
        "sponsor withholds a retention": "id=editFinancialAwardInfoForm:sponsorWitholdsRetention"
    }
    

    @classmethod
    def url(cls, segment_Id):
        """
        Direct navigation to SCR_648
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&FinancialAwardInformationEvent=&segmentId={}&formName=SegmentHomeForm"
        
        return url.format(segment_Id)
    
#     contact_search = Text("contact search", "Contact search")
#     salutation = Select("salutation", "Salutation")
#     first_name = Text("first name", "First name")
#     middle_name = Text("middle name", "Middle name")
#     last_name = Text("last name", "Last name")
#     suffix = Text("suffix", "Suffix")
#     address = Select("address", "Address")
#     phone_number = Text("phone number", "Phone number")
#     fax_number = Text("fax number", "Fax number")
#     reporting_email = Text("reporting email", "Reporting email")
#     contact_email = Text("contact email", "Contact email")
#     PO_number = Text("PO number", "PO number")
#     refund_balances = Select("refund of balances required", "Refund of balances required")
#     report_submission = Checkbox("report submission method", "Report submission method")
#     report_comment = Select("report submission comments", "Report submission method comments")
#     sponsor_approval = Select("sponsor's approval required for carryfoward", "Sponsor's approval required for carryfoward")
#     deliverable_schedule = Select("deliverable schedule", "Deliverable schedule")
#     delivery_billing = Select("deliverable must be met before billing", "Deliverable must be met before billing")
#     delivery_issued = Select("deliverable must be met before payment is issued", "Deliverable must be met before payment is issued")
#     delivery_comment = Select("deliverable schedule comment", "Deliverable schedule comment")
#     reportable_costshare = Select("reportable cost share", "Reportable cost share")
#     budget_restrictions = Select("budget restrictions", "Budget restrictions")
#     sponsor_withholds = Select("sponsor withholds a retention", "Sponsor withholds a retention")
#     
    
    contact_search = Text("contact search", "Contact search")
    salutation = Select("salutation", "Salutation")
    first_name = Text("first name", "First name")
    middle_name = Text("middle name", "Middle name")
    last_name = Text("last name", "Last name")
    suffix = Text("suffix", "Suffix")
    address = Select("address", "Address")
    phone_number = Text("phone number", "Phone number")
    fax_number = Text("fax number", "Fax number")
    reporting_email = Text("reporting email", "Reporting email")
    contact_email = Text("contact email", "Contact email")
    PO_number = Text("PO number", "PO number")
    refund_balances = Select("refund of balances required", "Refund of balances required")
    report_submission = Checkbox("report submission method", "Report submission method")
#     report_comment = Select("report submission comments", "Report submission method comments")
    sponsor_approval = Select("sponsor's approval required for carryfoward", "Sponsor's approval required for carryfoward")
    deliverable_schedule = Select("deliverable schedule", "Deliverable schedule")
#     delivery_billing = Radio("deliverable must be met before billing", "Deliverable must be met before billing")
#     delivery_issued = Radio("deliverable must be met before payment is issued", "Deliverable must be met before payment is issued")
#     delivery_comment = Text("deliverable schedule comment", "Deliverable schedule comment")
    reportable_costshare = Radio("reportable cost share", "Reportable cost share")
    budget_restrictions = Select("budget restrictions", "Budget restrictions")
    sponsor_withholds = Select("sponsor withholds a retention", "Sponsor withholds a retention")
        
        
 