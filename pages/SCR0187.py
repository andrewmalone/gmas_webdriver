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
        "income link": "event=IncomeEvent",
        "transfers": "event=IncomeEvent",
        "description": xpath.text_sibling("td", "Description", 2),
        "status": xpath.text_sibling("td", "Status", 2),
        "type": xpath.text_sibling("td", "Type", 2),
        "year": xpath.text_sibling("td", "Year", 2),
        "start date": "xpath=//*[contains(normalize-space(text()), 'Start date')]/ancestor::td[1]/following-sibling::td[2]",
        "end date": "xpath=//span[contains(normalize-space(text()), 'End date')]/../following-sibling::td[2]",
        "funds allocated": "xpath=//span[contains(normalize-space(text()), 'Funds allocated')]/../following-sibling::td[2]",
        "expended": "xpath=//a/span[contains(normalize-space(text()), 'Expended ($.00)')]/../../following-sibling::td[2]",
        "funds available": "xpath=//*[contains(normalize-space(text()), 'Funds available')]/ancestor::td[1]/following-sibling::td[2]",
        "income": "xpath=//a/span[contains(normalize-space(text()), 'Income ($.00')]/../../following-sibling::td[2]",
        "interest": "xpath=//a/span[contains(normalize-space(text()), 'Income ($.00')]/../../following-sibling::td[4]",
        "non-operating transfers": "xpath=//*[contains(normalize-space(text()), 'Non-operating transfers ($.00)')]/ancestor::td[1]/following-sibling::td[2]",
        "cash deficit": "xpath=//span[contains(normalize-space(text()), 'Cash deficit/(surplus)')]/../following-sibling::td[2]",
        "final figure": "xpath=//span[contains(normalize-space(text()), 'Final figure')]/../following-sibling::td[2]",
        "underspent": "xpath=//*[contains(normalize-space(text()), 'Underspent/(overspent)')]/ancestor::td[1]/following-sibling::td[2]",
        "account group": xpath.text_sibling("td", "Account group", 2),
        "research country": xpath.text_sibling("td", "Research country", 2),
        "campus location": xpath.text_sibling("td", "Campus Location", 2),
        "affiliate exchange": xpath.text_sibling("td", "Affiliate exchange account no.", 2),
        "locations": "xpath=//td[contains(normalize-space(text()), 'Research location')]/following-sibling::td[2]//tr[position() mod 2 = 1][position() > 1]",
        "HUID": xpath.text_sibling("td", "HU ID #", 2),
        "sequence": xpath.text_sibling("td", "Sequence ID #", 2),
        "indirect cost": xpath.text_sibling("td", "Indirect cost basis", 2),
        "at-risk amount": "xpath=//span[contains(normalize-space(text()), 'At-risk amount')]/../following-sibling::td[2]",
        "at-risk startdate": "xpath=//span[contains(normalize-space(text()), 'At-risk start date')]/../following-sibling::td[2]",
        "at-risk enddate": "xpath=//span[contains(normalize-space(text()), 'At-risk end date')]/../following-sibling::td[2]",
        "authorized per-award startdate": xpath.text_sibling("td", "Authorized pre-award start date", 2),
        "authorized pre-award direct cost amount": "xpath=//span[contains(normalize-space(text()), 'Authorized pre-award direct cost amount')]/../following-sibling::td[2]",
        "associated indirect cost amount": "xpath=//span[contains(normalize-space(text()), 'Associated indirect cost amount')]/../following-sibling::td[2]",
        "coa_rows": "xpath=//td[contains(text(),'Segment')]/../following-sibling::tr[@class='bg0']",
        "IDC_Rates": "xpath=//td[contains(text(), 'Indirect cost rates')]/ancestor::table[1]//tr[@class='bg0'][position()>2]",
        "comment_count": "xpath=//*[contains(normalize-space(text()), 'Comments')]/ancestor::td[1]/following-sibling::td[4]",
        "old_number": xpath.text_sibling("td", "Old number", 4)
    }

    _locators = {
        # "edit final figure": "EditAccountFinalFigureEvent",
        # "expenses": "event=ViewExpenseDetailsEvent",
        # "GL_history": "event=ViewGLHistoryEvent",
        # "fund": "event=ViewFundDetailsEvent",
        # "activity": "event=ViewActivityDetailsEvent",
        # "subactivity": "event=ViewSubactivityDetailsEvent",
        # "income": "event=IncomeEvent",
        # "transfers": "event=IncomeEvent",
        "description": "id=summaryDescription",
        "status": "id=summaryStatus",
        "type": "id=summaryType",
        "year": "id=summaryYear",
        # "start date": "xpath=//*[contains(normalize-space(text()), 'Start date')]/ancestor::td[1]/following-sibling::td[2]",
        # "end date": "xpath=//span[contains(normalize-space(text()), 'End date')]/../following-sibling::td[2]",
        "dates": "id=summaryDates",
        "funds allocated": "id=accountFinancialsFundsAllocated1",
        "expended": "id=accountFinancialsExpended",
        "funds available": "id=accountFinancialsFundsAvailable",
        "income": "xpath=//a[contains(normalize-space(text()), 'Income')]/../following-sibling::td[1]",
        "non-operating transfers": "id=accountFinancialsNoOperatingTransfers",
        "cash deficit": "id=accountFinancialsCashDeficit",
        "final figure": "xpath=//span[contains(normalize-space(text()), 'Final figure')]/../following-sibling::td[1]",
        "underspent": "id=accountFinancialsUnderspend",
        "account group": "id=additionalAccountInformationAccountGroup",
        "research country": "id=additionalAccountInformationResearchCountry",
        "campus location": "id=additionalAccountInformationCampusLocation",
        "affiliate exchange": "id=additionalAccountInformationAffiliateExchangeAccountNo2",
        "locations": "css=#accountResearchLocationsDataList_list li",
        "HUID": "id=additionalAccountInformationHUIDNum",
        "sequence": "id=additionalAccountInformationHUIDNum2",
        "indirect cost": "id=additionalAccountInformationIndirectCostBasis",
        "at-risk amount": xpath.text_sibling_child("td", "At-risk amount", 1),
        "at-risk startdate": xpath.text_sibling_child("td", "At-risk start", 1),
        "at-risk enddate": xpath.text_sibling_child("td", "At-risk end", 1),
        "authorized per-award startdate": xpath.text_sibling_child("td", "Pre-award start date", 1),
        "authorized pre-award direct cost amount": xpath.text_sibling_child("td", "Pre-award direct costs", 1),
        "associated indirect cost amount": xpath.text_sibling_child("td", "Pre-award indirect costs", 1),
        "coa_rows": "css=#chartOfAccountsGrid tr:nth-child(n+2)",
        "IDC_Rates": "css=#indirectCostRatesDatatable tbody tr",
        "comment_count": "css=a[id^=commentsLinkForm]",
        "old_number": xpath.text_sibling_child("td", "Old number", 4)
    }

    description = RText("description", "Account description")
    status = RText("status", "Account status")
    type = RText("type", "Account type")
    year = RText("year", "Account year")

    # # start_date = RText("start date", "Account start date")
    # # end_date = RText("end date", "Account end date")

    funds_allocated = RText("funds allocated", "funds allocated")
    expended = RText("expended", "expenses")
    funds_available = RText("funds available", "funds available")
    # income = RText("income", "income")
    transfers = RText("non-operating transfers", "non-operating transfers")
    cash_deficit = RText("cash deficit", "cash deficit/(surplus)")
    # final_figure = RText("final figure", "final figure amount")
    underspent = RText("underspent", "Underspent amount")

    account_group = RText("account group", "account group info")
    research_country = RText("research country", "research country info")
    campus_location = RText("campus location", "campus location info")
    affiliate_exchange = RText("affiliate exchange", "affiliated exchange account no")
    indirect_cost = RText("indirect cost", "indirect cost basis info")
    huid = RText("HUID", "HU ID #")
    sequence = RText("sequence", "Sequence #")

    # ------

    atrisk_amount = RText("at-risk amount", "at-risk amount info")
    atrisk_start = RText("at-risk startdate", "at-risk startdate info")
    atrisk_end = RText("at-risk enddate", "at-risk enddate info")
    preaward_start = RText("authorized per-award startdate", "authorized per-award startdate info")
    preaward_direct = RText("authorized pre-award direct cost amount", "authorized pre-award direct cost amount info")
    preaward_indirect = RText("associated indirect cost amount", "associated indirect cost amount")

    old_number = RText("old_number", "Old COA number")
    # PREAWARD!

    @classmethod
    def url(cls, segment_id, account_id):
        """
        Direct navigation to SCR_0187
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0360AccountsListForSegment.jsp&accountId={}&segmentId={}&formName=AccountsListForSegmentForm&ViewAccountDetailsEvent="
        return url.format(account_id, segment_id)

    @property
    def dates(self):
        """
        Account dates
        """
        if self.mode == "old":
            return "{} - {}".format(self.find("start date").text, self.find("end date").text)
        if self.mode == "convert":
            return self.find("dates").text

    @property
    def income(self):
        if self.mode == "old":
            return self.find("income").text
        if self.mode == "convert":
            return self.find("income").text.split(" (")[0]

    @property
    def interest(self):
        if self.mode == "old":
            return self.find("interest").text.replace("includes ", "").replace(" from interest", "")
        if self.mode == "convert":
            return self.find("income").text.split("(i")[1].replace("ncludes ", "").replace(" from interest)", "")

    @property
    def final_figure(self):
        text = self.find("final figure").text
        if "Edit" in text:
            text = text[:-5]
        return text

    @property
    def comment_count(self):
        if self.mode == "old":
            return self.find("comment_count").text.split(" ")[0]
        if self.mode == "convert":
            return self.find("comment_count").text.split(" (")[1][:-1]

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
        return self.go("income link")

    def goto_transfers(self):
        """
        Click the "Non-operating transfers" link
        Goes to SCR_0299
        """
        return self.go("transfers")

    @property
    def idc_rates(self):
        """
        Returns a list of IDC rate rows
        //IDC rate
        """
        return [self.IDC_Rates(row, self) for row in self.finds("IDC_Rates")]

    @property
    def locations(self):
        """
        Returns a list of account locations
        //Account_location
        """
        return [self.Account_location(row, self) for row in self.finds("locations")]

    class Account_location(Row):
        locators = {
            "location": Row.cell(1),
            "percent": Row.cell(2)
        }

        @property
        def location(self):
            if self.page.mode == "old":
                return self.find("location").text
            if self.page.mode == "convert":
                return self.driver.text.split(" (")[0]

        @property
        def percent(self):
            if self.page.mode == "old":
                return self.find("percent").text
            if self.page.mode == "convert":
                return self.driver.text.split(" (")[1].rstrip(")")

    class IDC_Rates(Row):
        locators = {
            "rate": Row.cell(6),
            "date": Row.cell(2),
            "gl_date": Row.cell(10)
        }
        _locators = {
            "rate": Row.cell(2),
            "date": Row.cell(1),
            "gl_date": Row.cell(3)
        }
        rate = RText("rate", "IDC Rate")
        date = RText("date", "IDC Effective Date")
        gl_date = RText("gl_date", "GL Effective Date")

    class COA_row(Row):
        locators = {
            "segment": Row.cell(2),
            "gl_status": Row.cell(6),
            "gl_feed": Row.cell(10),
            "value_descriptor": Row.cell(14)
        }
        _locators = {
            "segment": Row.cell(1),
            "gl_status": Row.cell(2),
            "gl_feed": Row.cell(3),
            "value_descriptor": Row.cell(4)
        }
        segment = RText("segment", "COA segment")
        gl_status = RText("gl_status", "GL status")
        gl_feed = RText("gl_feed", "GL feed")
        value_descriptor = RText("value_descriptor", "value and descriptor")
