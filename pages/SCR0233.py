from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0233(Page):
    """
    SCR_0233 Subagreement home
    """
    locators = {
        "documents": "link=Documents",
        "budget": "event=ViewSubagreementIssuedBudgetEvent",
        "openall": "link=open all",
        "amendment row": xpath.parent_row_of_event("ViewAmendmentEvent"),
        "status": xpath.text_sibling("td", "Subagreement attributes", 2),
        "sub_id": xpath.text_sibling("td", "Subagreement no.", 2),
        "sub_org": "event=ViewSubrecipientEvent",
        "description": xpath.text_sibling("td[@class='strong']", "Description", 2, element2="td"),
        "sub_pi": "event=ViewSubrecipientPIEvent",
        "issued_start": "xpath=//td[@class='strong'][text()='Subagreement attributes']/ancestor::table[2]//tr[17]/td[4]/table//tbody/tr/td[1]",
        "ant_start": "xpath=//td[@class='strong'][text()='Subagreement attributes']/ancestor::table[2]//tr[17]/td[4]/table//tbody/tr/td[2]",
        "issued_end": "xpath=//td[@class='strong'][text()='Subagreement attributes']/ancestor::table[2]//tr[19]/td[4]/table//tbody/tr/td[1]",
        "ant_end": "xpath=//td[@class='strong'][text()='Subagreement attributes']/ancestor::table[2]//tr[19]/td[4]/table//tbody/tr/td[2]",
        "issued_dollars": "xpath=//td[@class='strong'][text()='Subagreement attributes']/ancestor::table[2]//tr[21]/td[4]/table//tbody/tr/td[1]",
        "ant_dollars": "xpath=//td[@class='strong'][text()='Subagreement attributes']/ancestor::table[2]//tr[21]/td[4]/table//tbody/tr/td[2]",
        "amendment_summary": xpath.text_sibling("td[@class='strong']", "Subagreements and amendments", 2, element2="td"),
        "account_summary": "xpath=//td[@class='strong'][contains(text(), 'Subagreement') and contains(text(), 'accounts')]/following-sibling::td[2]",
        "account_row": "css=[id^=AccountsBlock][id$=CCBODY] tr.bg0:nth-of-type(n + 3)",
        "account_total_dollars": "css=#AccountsBlockBCCBODY tr.bg0:last-of-type td:nth-child(6)",
        "account_total_balance": "css=#AccountsBlockBCCBODY tr.bg0:last-of-type td:nth-child(10)",
        "proposed_start": xpath.text_sibling_child("td", "Proposed Start date", 2),
        "proposed_end": xpath.text_sibling("td", "Proposed End date", 2),
        "proposed_dollars": xpath.text_sibling_child("td", "Proposed Dollars", 2),
        "idc_row": "css=#SubrecipientRatesBlockCCBODY tr:nth-of-type(2n+4)",
        "sub_indirect_basis": xpath.text_sibling("td[@class='strong']", "Indirect basis", 2, element2="td"),
        "request_row": "css=#RequestsBlockCCBODY tr:nth-of-type(n+4):not(:last-of-type)",
        "notice_row": "css=#subagreementNoticesCCBODY tr:nth-of-type(2n+5):not(:last-of-type)",
        "notice_summary": xpath.text_sibling("td[@class='strong']", "Notices", 2, element2="td"),
        "request_summary": xpath.text_sibling("td[@class='strong']", "Requests", 2, element2="td"),
        "harvard_indirect_basis": xpath.text_sibling("td[@class='strong']", "Indirect Policy", 2, element2="td"),
        "harvard_idc_row": "css=#HarvardIDCRatesBlockCCBODY tr:nth-of-type(2n+8):not(:last-of-type)",
        "contact_row": "css=#SubrecipientContactsBlockCCBODY tr.bg0:not(:first-of-type)"
    }
    _locators = {
        # "documents": ,
        # "budget": ,
        "openall": "link=Open all",
        "amendment row": "css=#subagreementsAndAmendmentsDatatable tbody tr",
        "status": "id=summaryStatus",
        "sub_id": "css=h1",
        "sub_org": "event=ViewSubrecipientEvent",
        "description": "css=#summary li:nth-of-type(3)",
        "sub_pi": "event=ViewSubrecipientPIEvent",
        "issued_start": "id=subagreementIssuedStartDate",
        "ant_start": "id=subagreementAnticipatedStartDate",
        "issued_end": "id=subagreementIssuedEndDate",
        "ant_end": "id=subagreementAnticipatedEndDate",
        "issued_dollars": "id=subagreementIssuedDollars",
        "ant_dollars": "id=subagreementAnticipatedDollars",
        "amendment_summary": xpath.text_sibling("span[@class='ui-panel-title']", "Subagreements and amendments", 1, element2="ul"),
        "account_summary": xpath.text_sibling("span[@class='ui-panel-title']", "Subagreements accounts", 1, element2="ul"),
        "account_row": "css=.ui-panel-content:not([style='display:none']) #subagreementAccountsDatatable_data tr",
        "account_total_dollars": "css=.ui-panel-content:not([style='display:none']) #subagreementAccountsDatatable_foot tr td:nth-child(2)",
        "account_total_balance": "css=.ui-panel-content:not([style='display:none']) #subagreementAccountsDatatable_foot tr td:nth-child(3)",
        "proposed_start": "id=subagreementProposedStartDate",
        "proposed_end": "id=subagreementProposedEndDate",
        "proposed_dollars": "id=subagreementProposedDollars",
        "idc_row": "css=.ui-panel-content:not([style='display:none']) #subrecipientIndirectDatatable_data tr",
        "sub_indirect_basis": "css=#subrecipientIndirectBasisGrid td:last-of-type",
        "request_row": "css=.ui-panel-content:not([style='display:none']) #requestsDatatable_data tr",
        "notice_row": "css=.ui-panel-content:not([style='display:none']) #noticesDatatable_data tr",
        "notice_summary": xpath.text_sibling("span[@class='ui-panel-title']", "Notices", 1, element2="ul"),
        "request_summary": xpath.text_sibling("span[@class='ui-panel-title']", "Requests", 1, element2="ul"),
        "contact_row": "css=.ui-panel-content:not([style='display:none']) [id$=subrecipientContactsDatatable_data] tr"
    }

    # sub_id = RText("sub_id", "Subagreement number")
    sub_org = RText("sub_org", "Subagreement organization")
    #description = RText("description", "Subagreement description")
    sub_pi = RText("sub_pi", "Subagreement PI")
    issued_start = RText("issued_start", "Issued start date")
    issued_end = RText("issued_end", "Issued end date")
    issued_dollars = RText("issued_dollars", "Issued dollars")
    ant_start = RText("ant_start", "Anticipated start date")
    ant_end = RText("ant_end", "Anticipated end date")
    ant_dollars = RText("ant_dollars", "Anticipated dollars")
    proposed_start = RText("proposed_start", "Proposed start date")
    proposed_end = RText("proposed_end", "Proposed end date")
    proposed_dollars = RText("proposed_dollars", "Proposed dollars")
    account_total_dollars = RText("account_total_dollars", "Sum of account dollars")
    account_total_balance = RText("account_total_balance", "Sum of account balance")
    sub_indirect_basis = RText("sub_indirect_basis", "Subagreement indirect basis")
    # hvd_indirect_basis = RText("harvard_indirect_basis", "Harvard indirect policy")

    @classmethod
    def url(cls, segment_id, subagreement_id, subagreement_status_id):
        url = "{{}}/gmas/dispatch?ref=%2Fsubagreement%2FSCR0232SubagreementListWithinSegment.jsp&subagreementId={}&ViewSubagreementEvent=&segmentId={}&formName=SubagreementListForm&subagreementStatus={}"
        return url.format(subagreement_id, segment_id, subagreement_status_id)

    @property
    def sub_id(self):
        if self.mode == "old":
            return self.find("sub_id").text
        if self.mode == "convert":
            return self.find("sub_id").text.split(" ")[1]

    @property
    def description(self):
        if self.mode == "old":
            return self.find("description").text
        if self.mode == "convert":
            return self.find("description").text.replace("Description", "")

    @property
    def status(self):
        if self.mode == "old":
            text = self.find("status").text
            return text[9:]
        if self.mode == "convert":
            return self.find("status").text

    @property
    def amendment_summary(self):
        element = self.find("amendment_summary")
        if self.mode == "old":
            # return element.text.split(" | ")
            return element.text
        if self.mode == "convert":
            return " | ".join([el.text for el in element.find_elements_by_tag_name("li")])

    @property
    def account_summary(self):
        element = self.find("account_summary")
        if self.mode == "old":
            # return element.text.split(" | ")
            return element.text
        if self.mode == "convert":
            return " | ".join([el.text for el in element.find_elements_by_tag_name("li")])

    # @property
    # def notice_summary(self):
    #     element = self.find("notice_summary")
    #     if self.mode == "old":
    #         # return element.text.split(" | ")
    #         return element.text
    #     if self.mode == "convert":
    #         return " | ".join([el.text for el in element.find_elements_by_tag_name("li")])

    @property
    def request_summary(self):
        element = self.find("request_summary")
        if self.mode == "old":
            # return element.text.split(" | ")
            return element.text
        if self.mode == "convert":
            return " | ".join([el.text for el in element.find_elements_by_tag_name("li")])

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def goto_budget(self):
        """
        Clicks the <Subagreement detailed budget> button
        Goes to SCR_0428
        """
        return self.go("budget")

    def open_all(self):
        """
        Click the "open all" link
        """
        self.find("openall").click()

    @property
    def amendments(self):
        """
        Returns a list of amendments
        //Amendment_row
        """
        return [self.Amendment_row(row, self) for row in self.finds("amendment row")]

    @property
    def accounts(self):
        """
        Returns a list of accounts
        //Account_row
        """
        return [self.Account_row(row, self) for row in self.finds("account_row") if "Total" not in row.text]

    @property
    def sub_idc(self):
        """
        Returns a list of sub idc rates
        //IDC_row
        """
        return [self.IDC_row(row, self) for row in self.finds("idc_row") if "Indirect basis" not in row.text]

    @property
    def requests(self):
        return [self.Request_row(row, self) for row in self.finds("request_row")]

    @property
    def notices(self):
        return [self.Notice_row(row, self) for row in self.finds("notice_row")]

    @property
    def contacts(self):
        return [self.Contact_row(row, self) for row in self.finds("contact_row")]

    class Amendment_row(Row):
        locators = {
            "link": "event=ViewAmendmentEvent",
            "status": Row.cell(6),
            "dates": Row.cell(10),
            "dollars": Row.cell(14)
        }
        _locators = {
            "link": "event=ViewAmendmentEvent",
            "status": Row.cell(2),
            "dates": Row.cell(3),
            "dollars": Row.cell(4)
        }

        name = RText("link", "Amendment name")
        status = RText("status", "Amendment status")
        dates = RText("dates", "Amendment dates")
        dollars = RText("dollars", "Amendment dollars")

        def go(self):
            """
            Clicks the amendment link
            Goes to SCR_0240
            """
            return self._go("link")

    class Account_row(Row):
        locators = {
            "type": Row.cell(2),
            "description": Row.cell(6),
            "status": Row.cell(10),
            "string": Row.cell(14),
            "dollars": Row.cell(18),
            "balance": Row.cell(22)
        }
        _locators = {
            "type": Row.cell(1),
            "description": Row.cell(2),
            "status": Row.cell(3),
            "string": Row.cell(4),
            "dollars": Row.cell(5),
            "balance": Row.cell(6)
        }

        account_type = RText("type")
        # description = RText("description")
        status = RText("status")
        string = RText("string")
        dollars = RText("dollars")
        balance = RText("balance")

    class IDC_row(Row):
        locators = {
            "rate": Row.cell(2),
            "date": Row.cell(4)
        }
        _locators = {
            "rate": Row.cell(1),
            "date": Row.cell(2)
        }

        rate = RText("rate")
        date = RText("date")

    class Request_row(Row):
        locators = {
            "title": Row.cell(2),
            "status": Row.cell(6),
            "type": Row.cell(10),
            "dates": Row.cell(14),
            "dollars": Row.cell(18)
        }
        _locators = {
            "title": Row.cell(1),
            "status": Row.cell(2),
            "type": Row.cell(3),
            "dates": Row.cell(4),
            "dollars": Row.cell(5)
        }

        # title = RText("title")
        status = RText("status")
        type = RText("type")
        dates = RText("dates")
        dollars = RText("dollars")

    class Notice_row(Row):
        locators = {
            "title": Row.cell(2),
            "award_no": Row.cell(6),
            "amend": Row.cell(10),
            "received": Row.cell(14),
            "status": Row.cell(18)
        }
        _locators = {
            "title": Row.cell(1),
            "award_no": Row.cell(2),
            "amend": Row.cell(3),
            "received": Row.cell(4),
            "status": Row.cell(5)
        }

        # title = RText("title")
        award_no = RText("award_no")
        amend_no = RText("amend")
        date_received = RText("received")
        status = RText("status")

    class Contact_row(Row):
        locators = {
            "name": Row.cell(2),
            "type": Row.cell(6)
        }
        _locators = {
            "name": Row.cell(1),
            "type": Row.cell(2)
        }

        name = RText("name")
        type = RText("type")
