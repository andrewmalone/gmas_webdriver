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
        "revision comments": "xpath=//*[contains(normalize-space(text()), 'Revision comments')]/ancestor::tr[1]/following-sibling::tr[4]",
        "reason": "xpath=//*[contains(normalize-space(text()), 'Reason for administrative change or correction')]/ancestor::tr[1]/following-sibling::tr[3]",
        "award identifying information": xpath.text_sibling("td", "Award identifying information", 2),
        "sponsors": xpath.text_sibling("td", "Sponsors", 2),
        "awarded dates and dollars": xpath.text_sibling("td", "Awarded dates and dollars", 2),
        "allocation of awarded funds to accounts": xpath.text_sibling("td", "Allocation of awarded funds to accounts", 2),
        "accounts": xpath.text_sibling("td", "Accounts", 2),
        "cost sharing": xpath.text_sibling("td", "Cost sharing", 2),
        "approval attributes": xpath.text_sibling("td", "Approval attributes", 2),
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
    


    
    def open_all(self):
        """
        Click "open all"
        """
        return self.go("open_all")
