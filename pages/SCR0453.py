from pages.Page import Page
from pages.elements import Text, RText, Radio
import utilities.xpath as xpath


class SCR0453(Page):
    """
    SCR_0453 Edit notice attributes
    """
    locators = {
        "ok": "EditNoticeAttributesOkEvent",
        "title": "noticeTitle",
        "notice title": "css=input[name='noticeTitle']",
        "sponsor award no.": xpath.text_sibling("td", "Sponsor award no.", 2),
        "sponsorAwardExtra": "css=input[name='typeOfNumber']",
        "purchase oder": "name=purchaseOrderNumber",
        "form of notice": "css=input[name='formOfNotice']",
        "date issued": xpath.text_sibling("td", "Date issued", 2),
        "date received": xpath.text_sibling("td", "Date received by Harvard", 2),
        "date fully executed": xpath.text_sibling("td", "Date fully executed", 2),
        "Cancel": "css=input[name='EditNoticeAttributesCancelEvent']"
    }
    _locators = {

    }

    title = Text("title", "Notice title")
    notice_title = Text("notice title", "Notice Title")
    sponsor_award = Text("sponsor award no.", "Sponsor award no.")
    number_type = Radio("sponsorAwardExtra", "typeOfNumber")
    purchase_order = Text("purchase oder", "Purchase order no.")
    notice = Radio("form of notice", "formOfNotice")
    date_issued = Text("date issued", "Date issued")
    date_received = Text("date received", "Date received by harvard")
    date_executed = Text("date fully executed", "Date fully executed" )
    
    @classmethod
    def url(cls, segment_id, notice_id):
 
        """
        Direct navigation to SCR_0453
        """
        url = " {{}}/gmas/dispatch?&segmentId={}&noticeId={}&version=3&EditNoticeAttributesEvent.x=109&EditNoticeAttributesEvent.y=11&ref=%2Fnotice%2FSCR0309NoticeDetailsInclude.jsp&formName=NoticeForm"
        return url.format(segment_id, notice_id)
    
    
    def ok(self):
        """
        Clicks <Ok>
        Goes to SCR_0309
        """
        return self.go("ok")

