from pages.Page import Page
import utilities.xpath as xpath
from pages.elements import RText


class SCR0647(Page):
    """
    SCR_0647 Financial award information
    """
    locators = {
        "Edit_all": "xpath=//input[@name='projectForm:j_idt168']",
        "contact name": xpath.text_sibling("td", "Contact name:", 1),
        "address": xpath.text_sibling("td", "Address:", 1),
        "phone number": xpath.text_sibling("td", "Phone number:", 1),
        "report email": xpath.text_sibling("td", "Report email:", 1),
        "po number": xpath.text_sibling("td", "PO number:", 1),
        "refund of balances required": xpath.text_sibling("td", "Refund of balances required:", 1),
        "report submission method": xpath.text_sibling("td", "Report submission method:", 1),
        "sponsor's approval required for carryfoward": xpath.text_sibling("td", "Sponsor's approval required for carryfoward:", 1),
        "deliverable schedule": xpath.text_sibling("td", "Deliverable schedule:", 1),
        "reportable cost share": xpath.text_sibling("td", "Reportable cost share:", 1),
        "budget restrictions": xpath.text_sibling("td", "Budget restrictions:", 1),
        "sponsor withholds a retention": xpath.text_sibling("td", "Sponsor withholds a retention:", 1)
    }

    _locators = {
#         "contact name": "xpath=//span[@id='contactName']/.."
        "Edit_all": "css=[id$=editButton]",
        "contact name": xpath.text_sibling_child("td", "Contact name", 1),
        "address": xpath.text_sibling_child("td", "Address", 1),
        "phone number": xpath.text_sibling_child("td", "Phone number", 1),
        "report email": xpath.text_sibling_child("td", "Report email", 1),
        "po number": xpath.text_sibling_child("td", "PO number", 1),
        "refund of balances required": xpath.text_sibling_child("td", "Refund of balances required", 1),
        "report submission method": xpath.text_sibling_child("td", "Report submission method", 1),
        "sponsor's approval required for carryfoward": xpath.text_sibling_child("td", "Sponsor's approval required for carryfoward", 1),
        "deliverable schedule": xpath.text_sibling_child("td", "Deliverable schedule", 1),
        "reportable cost share": xpath.text_sibling_child("td", "Reportable cost share", 1),
        "budget restrictions": xpath.text_sibling_child("td", "Budget restrictions", 1),
        "sponsor withholds a retention": xpath.text_sibling_child("td", "Sponsor withholds a retention", 1)
    }

    
    @classmethod
    def url(cls, segment_id):
 
        """
        Direct navigation to SCR_0647
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&FinancialAwardInformationEvent=&segmentId={}&formName=SegmentHomeForm"
        return url.format(segment_id)
    
    def goto_editall(self):
            """
            Click the revision link
            Goes to SCR_0648
            """
            return self.go("Edit_all")


    contact_name = RText("contact name", "Financial contact name")
    address = RText("address", "Financial contact address")
    phone_number = RText("phone number", "Financial contact phone number")
    report_email = RText("report email", "Financial contact report email")
    po_number = RText("po number", "PO number")
    refund_balances = RText("refund of balances required", "Refund of balances required")
    report_submission = RText("report submission method", "Report submission method")
    sponsor_approval = RText("sponsor's approval required for carryfoward", "Sponsor's approval required for carryfoward")
    deliverable_schedule = RText("deliverable schedule", "Deliverable schedule")
    cost_share = RText("reportable cost share", "Reportable cost share")
    budget_restrictions = RText("budget restrictions", "Budget restrictions")
    sponsor_witholds = RText("sponsor withholds a retention", "Sponsor withholds a retention")
