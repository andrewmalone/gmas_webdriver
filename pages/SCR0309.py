from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath

class SCR0309(Page):
    """
    SCR_0309 Notice Home
    """
    locators = {
        "review completed": "ReviewCompletedEvent",
        "revise project": "CreateNewRevisionEvent",
        "documents": "link=Documents",
        "status": "xpath=//td[contains(text(), 'Notice status')]",
        "edit_attributes": "EditNoticeAttributesEvent",
        "notice title": xpath.text_sibling("td", "Notice Title", 2),
        "sponsor award no": xpath.text_sibling("td", "Sponsor award no.", 2),
        "amendment no": xpath.text_sibling("td", "Amendment no.", 2),
        "form of notice": xpath.text_sibling("td", "Form of notice", 2),
        "date issued": "xpath=//span[contains(normalize-space(text()), 'Date issued')]/../following-sibling::td[2]",
        "date received": "xpath=//span[contains(normalize-space(text()), 'Date received by Harvard')]/../following-sibling::td[2]",
        "date fully executed": "xpath=//span[contains(normalize-space(text()), 'Date fully executed')]/../following-sibling::td[2]",
        "request row": "xpath=//a[contains(@href,'RequestHomeEvent')]/ancestor::tr[1]",
        "document count": "xpath=//*[contains(normalize-space(text()), 'Documents')]/ancestor::td[1]/following-sibling::td[2]",
        "edit_associates": "EditRequestNoticeAssociationEvent"
    }
    
    _locators = {
        "status": "css=[id$=summaryStatus]",
        "edit_attributes": "css=div[id$=noticeAttributesPanel_header] div button",
        "notice title": "css=[id$=noticeAttributesNoticeTitle]",
        "sponsor award no": "css=[id$=noticeAttributesSponsorAwardNo]",
        "amendment no": "css=[id$=noticeAttributesAmendmentNo]" ,
        "form of notice": "css=[id$=noticeAttributesFormOfNotice]",
        "date issued": "css=[id$=noticeAttributesDateIssued]",
        "date received": "css=[id$=noticeAttributesDateReceivedBy]",
        "date fully executed": "css=[id$=noticeAttributesDateFullyExecuted]",
        "request row": "css=[id$=associatedRequestsPanel_content]",
        "document count": "xpath=//div[@id='j_idt118:documentsPanel_header']/ul/li/span",
        "edit_associates": "css=[id$=associatedRequestsPanel_header] div button",
        "action_memo": "css=[id$=actionMemoHistoryPanel_content]"
    }      
                 
                
    @classmethod
    def url(cls, notice_id, segment_id):
        """
        Direct navigation to SCR_0309
        """
        url = "{{}}/gmas/dispatch?ref=%2Fnotice%2FSCR0308ListofNoticesInASegment.jsp&noticeId={}&segmentId={}&formName=ListOfNoticesForm&ViewDetailsOfNoticeEvent=&submit"
        return url.format(notice_id, segment_id)
 
    notice_title = RText("notice title", "Notice Title")
    sponsor_awardno = RText("sponsor award no", "Sponsored award no")
    amendment_no = RText("amendment no", "Amendment no.")
    formof_notice = RText("form of notice", "Form of notice")
    date_issued = RText("date issued", "Date issued")
    date_received = RText("date received", "Date received by harvard")
    date_fullyexecuted = RText("date fully executed", "Date fully executed")
    document_count = RText("document count", "Documents count")

    @property
    def notice_status(self):
        """
        Status as displayed on the screen
        """
        return self.find("status").text.replace("Notice status: ", "")

    def review_completed(self):
        """
        Click <Review completed>
        Stays on SCR_0309
        """
        return self.go("review completed")

    def revise_project(self):
        """
        Click <Revise project based on this notice>
        Goes to SCR_0328
        """
        return self.go("revise project")

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def edit_attributes(self):
        """
        Clicks the <Edit notice attributes> button
        Goes to SCR_0453
        """
        return self.go("edit_attributes")

#     @property
#     def document_count(self):
#         """
#         Number of documents showing in the document component
#         """
#         count = self.find("document count").text
#         return int(count[:count.find(" ")])


    @property
    def document_count(self):
        if self.mode == "old":
            text = self.find("document count").text
            return text[:2]
        if self.mode == "convert":
            return self.find("document count").text
    
    def request(self, n):
        """
        Returns the nth request in the list
        //Request_row
        """
        row = self.finds("request row")[n - 1]
        return self.Request_row(row, self) 
    
    @property
    def requests(self):
        """
        Returns the nth request in the list
        //Reuest_row
        """
        return [self.Request_row(row, self) for row in self.finds("request row")]
    
    class Request_row(Row):
        locators = {
            "request title": Row.cell(2),
            "request type": Row.cell(6),
            "proposed dates": Row.cell(10),
            "proposed dollars": Row.cell(14),
            "submitted": Row.cell(18)
        }
        
        _locators = {
           
            "request title": Row.cell(1),
            "request type": Row.cell(2),
            "proposed dates": Row.cell(3),
            "proposed dollars": Row.cell(4),
            "submitted": Row.cell(5)
        }
        def go(self):
            """
            Click the request link
            Goes to SCR_0115
            """
            return self._go("link")
        request_title = RText("request title", "Request title")
        request_type = RText("request type", "Request type")
        proposed_dates = RText("proposed dates", "Proposed dates")
        Proposed_dollars = RText("proposed dollars", "Proposed dollars")
        submitted = RText("submitted", "Submitted")
        
        
        


