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
        "notification recipients": xpath.text_sibling("td", "Notification recipients", 2),
        "revise the segment":" xpath=//td[contains(text(), 'Revise the segment based on a sponsor notice')]",
        "sponsor legal title": xpath.text_sibling("td", "Sponsor legal title", 2),
        "sponsor award no": xpath.text_sibling("td", "Sponsor award no.", 2),
        "form of notice": xpath.text_sibling("td", "Form of notice", 2),
        "date issued": //span[contains(normalize-space(text()), 'Date issued')]/../following-sibling::td[2],
        "date received by harvard": xpath.text_sibling("td", "Date received by Harvard", 2),
        "date fully executed": xpath.text_sibling("td", "Date fully executed", 2),
        "revision comments": "xpath=//*[contains(normalize-space(text()), 'Revision comments')]/ancestor::tr[1]/following-sibling::tr[4]",
        "reason": "xpath=//*[contains(normalize-space(text()), 'Reason for administrative change or correction')]/ancestor::tr[1]/following-sibling::tr[3]",
        "award identifying information": xpath.text_sibling("td", "Award identifying information", 2),
        "sponsors": xpath.text_sibling("td", "Sponsors", 2),
        "awarded_row": "xpath=//td[contains(text(), 'Budget period (mm-dd-yyyy)')]/ancestor::table[1]//tr[not (@class ='bg0')][position()>4]",
        "allocation_row": "xpath=//td[contains(text(), 'Grp.')]/ancestor::table[1]//tr[not (@class ='bg0')][position()>2]"
        "allocation of awarded funds to accounts": xpath.text_sibling("td", "Allocation of awarded funds to accounts", 2),
        "accounts": xpath.text_sibling("td", "Accounts", 2),
        "cost sharing": xpath.text_sibling("td", "Cost sharing", 2),
        "approval attributes": xpath.text_sibling("td", "Approval attributes", 2),
        "total fund authorized to pending subagreements": xpath.text_sibling_child("td", "Total funds authorized to pending subagreements", 2)
        "estimated Harvard University overhead for subagreements": xpath.text_sibling_child("td", "Estimated Harvard University overhead for subagreements", 2)
        "subagreements_row": "xpath=//td[contains(text(), 'Subagreements')]/ancestor::table[1]//tr[not (@class ='bg0')][position()>3]"
    }
    
    @classmethod
    def url(cls, segment_id, revision_id):
        """
        Direct navigation to SCR_0426
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Frevision%2FSCR0425RevisionsList.jsp&segmentId={}&formName=ListOfRevisionsForm&noBusinessLock=true&segmentRevisionId={}&ListOfRevisionsAppliedRevisionDetailEvent=&submit"
        return url.format(segment_id, revision_id)
    
    
    
    date_initiated = RText("date initiated", "Date initiated")
    date_committed = RText("date committed", "Date committed")
    revision_id = RText("revision id", "Revision id")
    created_by = RText("created by", "Created by")
    committed_by = RText("committed by", "Committed by")
    type = RText("type", "Type")
    status = RText("status", "Status")
    notification_recipients = RText("notification recipients", "Notification recipients")
    revision_comments = RText("revision comments", "Revision comments")
    reason = RText("reason", "Reason")
    award_information = RText("award identifying information", "Award identifying information")
    sponsors = RText("sponsors", "Sponsors")
    awarded_dateanddollars = RText("awarded dates and dollars", "Awarded dates and dollars")
    allocation_awardedfunds = RText("allocation of awarded funds to accounts", "Allocation of awarded funds to accounts")
    accounts = RText("accounts", "Accounts")
    cost_sharing = RText("cost sharing", "Cost sharing")
    approval_attributes =  RText("approval attributes", "Approval attributes")
    total fund authorized to pending subagreements = RText("total fund authorized to pending subagreements", "Total fund authorized to pending subagreements")
    estimated Harvard University overhead for subagreements = RText("estimated Harvard University overhead for subagreements", "Estimated Harvard University overhead for subagreements")
    


    
    def open_all(self):
        """
        Click "open all"
        """
        return self.go("open_all")
    
    class Awarded_row(row):
        locators = {
            "budget": Row.cell(2)
            "obligated_current": Row.cell(6)
            "obligated_change": Row.cell(10)
            "obligated_total": Row.cell(14)
            "anticipated_current": Row.cell(18)
            "anticipated_change": Row.cell(22)
            "anticiapted_total": Row.cell(26)
            "carried forward_current": Row.cell(30)
            "carried forward_change": Row.cell(34)
            "carried forward_total": Row.cell(38)
    }
    
        budget = RText("budget", "Budget  period")
        obligated_current = RText("obligated_current", "obligated_current")
        obligated_change = RText("obligated_total","obligated_total")
        obligated_total = RText("obligated_total", "obligated_total")
        anticipated_current = RText("anticipated_current", "anticipated_current")
        anticipated_change = RText("anticipated_change", "anticipated_change" )
        anticiapted_total = RText("anticiapted_total", "anticiapted_total")
        carried forward_current = RText("carried forward_current","carried forward_current")
        carried forward_change = RText("carried forward_change", "carried forward_change")
        carried forward_total = RText("carried forward_total", "carried forward_total")
        
    class Allocation_row(row):
        locators = {
            "grp": Row.cell(2) 
            "account(s)": Row.cell(6)
            "type": Row.cell(10)
            "description": Row.cell(14)
            "current": Row.cell(18)
            "change": Row.cell(22)
            "total": Row.cell(26)
        } 
        
        grp = RText("grp", "Grp")
        account(s) = RText("account(s)", "Accounts(s)")
        type = RText("type", "Type")
        description = RText("description", "Description")
        current = RText("current", "Current($.00)")
        change = RText("change", "Change($.00)")
        total = RText("total", "Total($.00)")
    class Subagreements_row(row):
        locators = {
             "subrecipient": Row.cell(2)
             "authorized, non-issued funds": Row.cell(6)
             "estimated HU overhead": Row.cell(10)    
             }
        
        subrecipient = RText("subrecipient", "Subrecipient")
        authorized_funds = RText("authorized, non-issued funds", "Authorized, non-issued funds")
        estimated_overhead = RText("estimated HU overhead", "Estimated HU overhead")
                    
                    
                    
                    
        
        
        
        
        
