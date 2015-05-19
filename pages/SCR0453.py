from pages.Page import Page
from pages.elements import Text, Radio
import utilities.xpath as xpath


class SCR0453(Page):
    """
    SCR_0453 Edit notice attributes
    """
    locators = {
        "ok": "EditNoticeAttributesOkEvent",
        "title": "noticeTitle",
        "sponsor award no.": "css=input[name='sponsorAwardNumber']",
        "number type": "css=input[name='typeOfNumber']",
        "purchase order": "css=input[name='purchaseOrderNumber']",
        "form of notice": "css=input[name='formOfNotice']",
        "date issued": "css=input[name='dateIssued']",
        "date received": "css=input[name='dateReceivedByHarvard']",
        "date fully executed":"css=input[name='dateFullyExecuted']",
        "Cancel": "css=input[name='EditNoticeAttributesCancelEvent']"
    }

    _locators = {
        "title": "css=[id$=noticeTitle]",
       "sponsor award no.": "css=[id$=sponsorAward]",
       "number type": "sponsorAward",
       "purchase order": "css=[id$=purchaseOrder]",
       "form of notice": "formOfNotice",
       "date issued": "css=[id$=dateIssued_input]",
       "date received": "css=[id$=dateReceivedBy_input]",
       "date fully executed":"css=[id$=dateFully_input]",
    }
    
    @classmethod
    def url(cls, segment_id, notice_id):
 
        """
        Direct navigation to SCR_0453
        """
        url = "{{}}/gmas/dispatch?&segmentId={}&noticeId={}&version=3&EditNoticeAttributesEvent.x=109&EditNoticeAttributesEvent.y=11&ref=%2Fnotice%2FSCR0309NoticeDetailsInclude.jsp&formName=NoticeForm"
        return url.format(segment_id, notice_id)

    title = Text("title", "Notice title")
    sponsor_award = Text("sponsor award no.", "Sponsor award no.")
    number_type = Radio("number type", "typeOfNumber")
    purchase_order = Text("purchase order", "Purchase order no.")
    notice = Radio("form of notice", "formOfNotice")
    date_issued = Text("date issued", "Date issued")
    date_received = Text("date received", "Date received by harvard")
    date_executed = Text("date fully executed", "Date fully executed" )
     
    def ok(self):
        """
        Clicks <Ok>
        Goes to SCR_0309
        """
        return self.go("ok")

