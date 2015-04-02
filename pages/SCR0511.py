from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0511(Page):
    """
    SCR_0511 subactivity detail
    """
    locators = {
            "disable": "DisableSubactivityEvent",
            "reenable": "ReenableSubactivityEvent",
            "subactivity_information": "xpath=//td[contains(text(), 'Subactivity information')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
            "gl_upload_history": "xpath=//td[contains(text(), 'General ledger upload history')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
            "gl status": xpath.text_sibling("td", "General ledger status", 2),
            "owning tub": xpath.text_sibling("td", "Owning tub", 2),
            "description": xpath.text_sibling("td", "Description", 2),
            "year": xpath.text_sibling("td", "Year", 2)
    }

    @classmethod
    def url(cls, account_id, segment_id, subactivity_id, fund):
        """
        Direct navigation to scr0511
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0187AccountDetail.jsp&accountId={}&segmentId={}&formName=AccountDetailForm&subactivityId={}&fund={}&ViewSubactivityDetailsEvent=&submit"
        return url.format(account_id, segment_id, subactivity_id, fund)
    
    gl_status = RText("gl status", "General ledger status")
    owning_tub = RText("owning tub", "Owning tub")
    description = RText("description", "Description")
    year = RText("year", "Year")
    
    def disable(self):
        """
        Click the <Disable subactivity> button
        Goes to SCR_0602a or stays on the current page with an error
        """
        return self.go("disable")

    def reenable(self):
        """
        Click the <Re-enable subactivity> button
        Goes to SCR_0625a
        """
        return self.go("reenable")
   
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
        date = RText("date", "GL date")
        type = RText("type", "GL action type")
        feed_status = RText("feed_status", "GL feed status")

    
