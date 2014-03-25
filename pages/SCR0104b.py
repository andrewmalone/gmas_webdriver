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
    "segment documents": "event=SegmentDocumentsLinkEvent"
}


class SCR0104b(Page):
    """
    SCR_0104b Segment Home
    """
    locators = locators

    @property
    def document_count(self):
        """
        Number of documents showing in the document component
        """
        count = self.find("document count").text
        return int(count[:count.find(" ")])

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
        #self.driver.find_element_by_css_selector(locators["make revision"]).click()
        self.find_element(locators["make revision"]).click()
        self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0105]"))
        from pages.SCR0105 import SCR0105
        return SCR0105(self.driver)

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
        return self.go("documents")
	
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
