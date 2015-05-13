from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0191(Page):
    """
    SCR_0191 Fund detail
    """

    locators = {
            "Disable_fund": "DisableFundEvent",
            "Reenable_fund": "ReenableFundEvent",
            "Fund_info": "xpath=//td[contains(text(), 'General ledger status')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
            "GL_history": "xpath=//td[contains(text(), 'General ledger upload history')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
            "gl status": xpath.text_sibling("td", "General ledger status", 2),
            "owning tub": xpath.text_sibling("td", "Owning tub", 2),
            "owning org": xpath.text_sibling("td", "Owning org", 2),
            "funding category": xpath.text_sibling("td", "Funding category", 2),
            "funding type":  xpath.text_sibling("td", "Funding type", 2),
            "agency fund":  xpath.text_sibling("td", "Agency fund", 2),
            "gift":  xpath.text_sibling("td", "Gift or interest override", 2),
            "keyword": xpath.text_sibling("td", "Keyword", 2)
    }
        
    _locators = {
                 
                 "Fund_title": "css=[id=actionbar_content] tbody tr",
                 "descriptor": "css=[id$=descriptor]",
                 "gl status": "css=[id$=GLStatus]",
                 "owning tub": "css=[id$=tubDescriptor]",
                 "owning org": "css=[id$=orgDescriptor]",
                 "funding category": "css=[id$=fundcategory]",
                 "funding type": "css=[id$=fundType]",
                 "agency fund": "css=[id$=agencyFund]",
                 "gift": "css=[id$=giftOrInterestOverride]",
                 "keyword": "css=[id$=keyWord]",
                 "GL_history": "css=[id$=GLUploadHistory_content] tbody tr"
    }
    
    @classmethod
    def url(cls, account_id, segment_id, fund):
        """
        Direct navigation to SCR_0191
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0187AccountDetail.jsp&accountId={}&segmentId={}&formName=AccountDetailForm&fund={}&ViewFundDetailsEvent=&submit"
        return url.format(account_id, segment_id, fund)

    gl_status = RText("gl status", "General ledger status")
    owning_tub = RText("owning tub", "Owning tub")
    owning_org = RText("owning org", "Fund Owning org")
    catogery = RText("funding category", "Funding category")
    type = RText("funding type", "Funding type")
    agency = RText("agency fund", "Agency fund")
    gift = RText("gift", "Gift or interest override")
    keyword = RText("keyword", "Keyword")

    @property
    def gl_history(self):
        """
        Returns a list of gl history rows
        //GL_history
        """
        return [self.GL_history(row, self) for row in self.finds("GL_history")]

    class GL_history(Row):
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
