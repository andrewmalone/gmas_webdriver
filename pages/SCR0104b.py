from pages.Page import Page
import utilities.xpath as xpath

locators = {
    "make revision": 'css=a[href*=SegmentHomeMakeRevisionEvent]',
    "continue revision": "css=a[href*='SegmentHomeEditRevisionEvent']",
    "confirm research team": "css=img[alt='Confirm research team']",
    "create request": "css=a[href*='SegmentHomeCreateRequestEvent']",
    "documents": "event=RepositoryLinkEvent",
    "document count": "xpath=(//a[contains(@href,'RepositoryLinkEvent')])[1]/ancestor::tr[1]/td[4]",
    "approvals": "event=ApprovalListHomeEvent",
    "notices": "event=ViewNoticeListEvent",
    "subagreements": "event=SubagreementsLinkEvent",
    "research team": "event=ResearchStaffLinkEvent",
    "admin team": "css=a[href*=SegmentSummaryAdministrativeTeamLinkEvent]",
    "requests": "css=a[href*=RequestListEvent]",
    "accounts": "event=AccountsLinkEvent",
    "segment documents": "event=SegmentDocumentsLinkEvent",
    "revisions": "event=SegmentHomeRevisionListEvent",
    "event history": "event=SegmentSummaryViewProjectHistoryLinkEvent",
    "todos": "event=SegmentSummaryViewProjectToDosLinkEvent",
    "project_info": xpath.text_sibling("td", "Project Information", 2),
    "dates_dollars": "event=SegmentHomeViewDatesAndDollarsEvent",
    "additional info": "event=AdditionalAwardInformationEvent",
    "fin award info": "event=FinancialAwardInformationEvent"
}

_locators = {
    "document_button": "css=.ui-menubutton.documents button",
    "segment_repository": "event=RepositoryLinkEvent",
    "requests": "css=a[href*=RequestListEvent]",
    "make revision": 'css=a[href*=SegmentHomeMakeRevisionEvent]',
}


class SCR0104b(Page):
    """
    SCR_0104b Segment Home
    """
    locators = locators
    _locators = _locators

    @property
    def document_count(self):
        """
        Number of documents showing in the document component
        """
        count = self.find("document count").text
        return int(count[:count.find(" ")])

    @property
    def status(self):
        """
        Segment status
        """
        text = self.find("project_info").text
        return text[text.index("|") + 2:]

    def nav_to(self, segment_id):
        """
        Direct navigation to a segment home (based on segment id)
        """
        url = "https://%s.harvard.edu/gmas/project/SCR0104SegmentHome.jsp?segmentId=%s" % (self.env, segment_id)
        self.driver.get(url)
        return SCR0104b(self.driver)

    def make_revision(self):
        """
        Click the <Make revision> button
        Goes to SCR_0105 (through the wait screen)
        """
        return self.action("make revision")

    def create_request(self):
        """
        Clicks the <Create request> button
        Goes to SCR_0472
        """
        return self.go("create request")

    def continue_revision(self):
        """
        Clicks the "continue making changes" link for an open revision
        Goes to SCR_0105
        """
        self.find("continue revision").click()
        return self.load_page()

    def confirm_research_team(self):
        """
        Clicks the <Confirm research team> button
        Goes to SCR_0645
        """
        return self.go("confirm research team")

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        if self.mode == "old":
            return self.go("documents")
        elif self.mode == "convert":
            self.find("document_button").click()
            return self.go("segment_repository")

    def goto_dates_dollars(self):
        """
        Clicks the "Dates and Dollars" link
        Goes to SCR_0070
        """
        return self.go("dates_dollars")

    def goto_additional_info(self):
        """
        Clicks the "Additional award information" link
        Goes to SCR_0519
        """
        return self.go("additional info")

    def goto_approvals(self):
        """
        Clicks the "Approvals" link
        Goes to SCR_0080
        """
        return self.go("approvals")

    def goto_notices(self):
        """
        Clicks the "Sponsor notices" link
        Goes to SCR_0308
        """
        return self.go("notices")

    def goto_subagreements(self):
        """
        Clicks the "Subagreements" link
        Goes to SCR_0232
        """
        return self.go("subagreements")

    def goto_research_team(self):
        """
        Clicks the "Research staff" link
        Goes to SCR_0015
        """
        return self.go("research team")

    def goto_admin_team(self):
        """
        Clicks the "Administrative team" link
        Goes to SCR_0300
        """
        return self.go("admin team")

    def goto_requests(self):
        """
        Clicks the "Requests" link
        Goes to SCR_0344
        """
        return self.go("requests")

    def goto_accounts(self):
        """
        Clicks the "Accounts" link
        Goes to SCR_0360
        """
        return self.go("accounts")

    def goto_segment_documents(self):
        """
        Clicks the "Segment documents" link
        Goes to SCR_0634
        """
        return self.go("segment documents")

    def goto_revisions(self):
        """
        Clicks the "Revisions" link
        Goes to SCR_0425
        """
        return self.go("revisions")

    def goto_event_history(self):
        """
        Clicks the "Event history" link
        Goes to SCR_0002
        """
        return self.go("event history")

    def goto_todos(self):
        """
        Clicks the "Segment to-do's" link
        Goes to SCR_0159
        """
        return self.go("todos")

    def goto_financial_award_info(self):
        """
        Clicks the "Financial award information" link
        Goes to SCR_0647
        """
        return self.go("fin award info")
