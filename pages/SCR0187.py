from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0187(Page):
    """
    SCR_0187 Account detail
    """
    locators = {
        "edit final figure": "EditAccountFinalFigureEvent",
        "expenses": "event=ViewExpenseDetailsEvent",
        "GL_history": "event=ViewGLHistoryEvent",
        "fund": "event=ViewFundDetailsEvent",
        "activity": "event=ViewActivityDetailsEvent",
        "subactivity": "event=ViewSubactivityDetailsEvent",
        "income": "event=IncomeEvent",
        "transfers": "event=IncomeEvent",
        "description": xpath.text_sibling("td", "Description", 2),
        "status": xpath.text_sibling("td", "Status", 2),
        "type": xpath.text_sibling("td", "Type", 2),
        "year": xpath.text_sibling("td", "Year", 2),
        "start date": "xpath=//*[contains(normalize-space(text()), 'Start date')]/ancestor::td[1]/following-sibling::td[2]",
        "end date": "xpath=//span[contains(normalize-space(text()), 'End date')]/../following-sibling::td[2]",
        "funds allocated": "xpath=//span[contains(normalize-space(text()), 'Funds allocated')]/../following-sibling::td[2]",
        "expended":"xpath=//a/span[contains(normalize-space(text()), 'Expended ($.00)')]/../../following-sibling::td[2]",
        "funds available": "xpath=//*[contains(normalize-space(text()), 'Funds available')]/ancestor::td[1]/following-sibling::td[2]",
        "income": "xpath=//a/span[contains(normalize-space(text()), 'Income ($.00')]/../../following-sibling::td[2]",
        "non-operating transfers": "xpath=//*[contains(normalize-space(text()), 'Non-operating transfers ($.00)')]/ancestor::td[1]/following-sibling::td[2]",
        "cash deficit":"xpath=//span[contains(normalize-space(text()), 'Cash deficit/(surplus)')]/../following-sibling::td[2]",
        "final figure": "xpath=//span[contains(normalize-space(text()), 'Final figure')]/../following-sibling::td[2]",
        "underspent": "xpath=//*[contains(normalize-space(text()), 'Underspent/(overspent)')]/ancestor::td[1]/following-sibling::td[2]",
        "account group": xpath.text_sibling("td", "Account group", 2),
        "research country": xpath.text_sibling("td", "Research country", 2),
        "campus location": xpath.text_sibling("td", "Campus Location", 2),
        "affiliate exchange": xpath.text_sibling("td", "Affiliate exchange account no.", 2),
        "indirect cost": xpath.text_sibling("td", "Indirect cost basis", 2),
        "at-risk amount": "xpath=//span[contains(normalize-space(text()), 'At-risk amount')]/../following-sibling::td[2]",
        "at-risk startdate": "xpath=//span[contains(normalize-space(text()), 'At-risk start date')]/../following-sibling::td[2]",
        "at-risk enddate": "xpath=//span[contains(normalize-space(text()), 'At-risk end date')]/../following-sibling::td[2]",
        "authorized per-award startdate": xpath.text_sibling("td", "Authorized pre-award start date", 2),
        "authorized pre-award direct cost amount": "xpath=//span[contains(normalize-space(text()), 'Authorized pre-award direct cost amount')]/../following-sibling::td[2]",
        "associated indirect cost amount":"xpath=//span[contains(normalize-space(text()), 'Associated indirect cost amount')]/../following-sibling::td[2]",
        "coa_rows": "xpath=//td[contains(text(), 'Chart of accounts')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
        "IDC_Rates": "xpath=//td[contains(text(), 'Indirect cost rates')]/ancestor::table[1]//tr[@class='bg0'][position()>2]",
        "comment_count": "xpath=//*[contains(normalize-space(text()), 'Comments')]/ancestor::td[1]/following-sibling::td[4]"
    
    }
    
    description = RText("description", "Account description")
    status = RText("status", "Account status")
    type = RText("type", "Account type")
    year = RText("year", "Account year")
    start_date = RText("start date", "Account start date")
    end_date = RText("end date", "Account end date")
    funds_allocated = RText("funds allocated", "funds allocated")
    expended = RText("expended", "expenses")
    funds_available = RText("funds available", "funds available")
    income = RText("income", "income")
    transfers = RText("non-operating transfers", "non-operating transfers")
    cash_deficit = RText("cash deficit", "cash deficit/(surplus)")
    final_figure = RText("final figure", "final figure amount")
    underspent = RText("underspent", "Underspent amount")
    account_group = RText("account group", "account group info")
    research_country = RText("research country", "research country info")
    campus_loaction = RText("campus location", "campus location info")
    affiliate_exchange = RText("affiliate exchange", "affiliated exchange account no")
    indirect_cost = RText("indirect cost", "indirect cost basis info")
    atrisk_amount = RText("at-risk amount", "at-risk amount info")
    atrisk_startdate = RText("at-risk startdate", "at-risk startdate info")
    atrisk_enddate = RText("at-risk enddate", "at-risk enddate info")
    authorized_startdate = RText("authorized per-award startdate", "authorized per-award startdate info")
    authorized_directcost = RText("authorized pre-award direct cost amount", "authorized pre-award direct cost amount info")
    associated_indirectcost = RText("associated indirect cost amount", "associated indirect cost amount")
    comments_count = RText("comment_count", "comment_count")
    
        
    @classmethod
    def url(cls, segment_id, account_id):
        """
        Direct navigation to SCR_0187
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0360AccountsListForSegment.jsp&accountId={}&segmentId={}&formName=AccountsListForSegmentForm&ViewAccountDetailsEvent="
        return url.format(account_id, segment_id)
    
    @property
    def tub(self):
        """
        authorized tub
        //COA_row
        """
        return self.COA_row(self.finds('coa_rows')[0], self)
    
    @property
    def org(self):
        """
        authorized org
        //COA_row
        """
        return self.COA_row(self.finds('coa_rows')[1], self)
    
    @property
    def fund(self):
        """
        Fund data
        //COA_row
        """
        return self.COA_row(self.finds('coa_rows')[2], self) 
    
    @property    
    def activity(self):
        """
        Activity data
        //COA_row
        """
        return self.COA_row(self.finds('coa_rows')[3], self)
    
    @property
    def subactivity(self):
        """
        Subactivity data
        //COA_row
        """
        return self.COA_row(self.finds('coa_rows')[4], self)
    
    @property
    def root(self):
        """
        Authorized root
        //COA_row
        """
        return self.COA_row(self.finds('coa_rows')[5], self)
    
    @property                    
    def gl_history(self):
        """
        Returns a list of gl history rows
        //GL_history
        """
        return [self.GL__history(row, self) for row in self.finds("GL_history")]

    
    def goto_expenses(self):
        """
        Click the "Expenses" link
        Goes to SCR_0072
        """
        return self.go("expenses")
     
     
    def goto_gl_history(self):
        """
        Click the "View GL History" link
        Goes to SCR_0560
        """
        return self.go("gl history")
     
     
    def goto_fund(self):
        """
        Click the fund link
        Goes to SCR_0191
         """
        return self.go("fund")
     
     
    def goto_activity(self):
        """
        Click the activity link
        Goes to SCR_0192
        """
        return self.go("activity")
     
     
    def goto_subactivity(self):
        """
        Click the subactivity link
        Goes to SCR_0511
        """
        return self.go("subactivity")
     
     
    def goto_income(self):
        """
        Click the "Income" link
        Goes to SCR_0299
        """
        return self.go("income")
     
     
    def goto_transfers(self):
        """
        Click the "Non-operating transfers" link
        Goes to SCR_0299
        """
        return self.go("transfers")
    
    @property
    def IDC_rates(self):
        """
        Returns a list of IDC rate rows
        //IDC rate
        """
        return [self.IDC_Rates(row, self) for row in self.finds("IDC_Rates")]
    
   
    class IDC_Rates(Row): 
        locators = {
            "rate":Row.cell(2),
            "date":Row.cell(6),
            "gl_date":Row.cell(10)
        }
        rate = RText("rate", "IDC Rate")
        date = RText("date", "IDC Effective Date")
        gl_date = RText("gl_date", "GL Effective Date")
    
    class COA_row(Row):
        locators = {
            "segment":Row.cell(2),
            "gl_status":Row.cell(6),
            "gl_feed":Row.cell(10),
            "value_descriptor":Row.cell(14)
        }
        segment = RText("segment", "COA segment")
        gl_status = RText("gl_status", "GL status")
        gl_feed = RText("gl_feed", "GL feed")
        value_descriptor = RText("value_descriptor", "value and descriptor")
        
        
        
        
        
        
            
              
                
                    

        
            
        
        
        