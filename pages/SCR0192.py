from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0192(Page):
    """
    SCR_0192 Activity detail
    """
    locators = {
            "Activity_information": "xpath=//td[contains(text(), 'Activity information')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
            "GL_upload_history": "xpath=//td[contains(text(), 'General ledger upload history')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
            "gl status": xpath.text_sibling("td", "General ledger status", 2),
            "owning tub": xpath.text_sibling("td", "Owning tub", 2),
            "owning org": xpath.text_sibling("td", "Owning org", 2),
            "activity type": xpath.text_sibling("td", "Activity type", 2),
            "OMB A-21 func.code": xpath.text_sibling("td", "OMB A-21 func. code", 2),
            "Keyword": xpath.text_sibling("td", "Keyword", 2)
    }
    
    _locators = {
            "GL_upload_history": "css=[id$=GLUploadHistoryPanel_content] tbody tr",
            "gl status": "css=[id$=GLStatus]",
            "owning tub": "css=[id$=Tub]",
            "owning org": "css=[id$=Org]",
            "activity type": "css=[id$=Type]",
            "OMB A-21 func.code": "css=[id$=A21Code]",
            "Keyword": "css=[id$=Keyword]" 
    }

    @classmethod
    def url(cls, account_id, segment_id, activity):
        """
        Direct navigate to SCR_0192
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0187AccountDetail.jsp&accountId={}&ViewActivityDetailsEvent=&segmentId={}&formName=AccountDetailForm&activity={}&submit"
        return url.format(account_id, segment_id, activity)
    
    
    gl_status = RText("gl status", "General ledger status")
    owning_tub = RText("owning tub", "Owning tub")
    owning_org = RText("owning org", "Fund Owning org")
    activity_type = RText("activity type", "activity type")
    omb_code = RText("OMB A-21 func.code", "OMB A-21 func.code")
    keyword = RText("Keyword", "Keyword")

    @property
    def gl_upload_history(self):
        """
        Returns a list of GL upload history rows
        //GL_upload_history
        """
        return [self.GL_upload_history(row, self) for row in self.finds("GL_upload_history")]

    class GL_upload_history(Row):
        locators = {
            "date": Row.cell(2),
            "type": Row.cell(6),
            "feed_status": Row.cell(10)
        }
        
        _locators = {
            "date": Row.cell(1),
            "type": Row.cell(2),
            "feed_status": Row.cell(3)
        }
        
        date = RText("date", "GL date")
        type = RText("type", "GL action type")
        feed_status = RText("feed_status", "GL feed status")
