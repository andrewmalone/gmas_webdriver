from pages.Page import Page

locators = {
    # "document count": "sizzle=td:contains('Document(s)'):not(td:has('table'))",
    "document count": "xpath=//div[@id='DocRepositoryComponentCCBODY']/preceding-sibling::*[1]//tr[1]/td[4]",
    "research staff": "link=Research staff",
    "initiate review": "css=a[href*='InitiateInternalReviewEvent'] img",
    "submit": "css=a[href*='SubmitToSponsorEvent'] img",
    "log notice": "css=img[alt='Log notice']",
    "edit budget": "css=a[href*='EditProposedDollarsSummaryBudgetEvent'] img"
}


class SCR0115(Page):
    locators = locators

    def nav_to(self, segment_id, request_id):
        url = "https://%s.harvard.edu/gmas/request/SCR0115Request.jsp?requestId=%s&segmentId=%s" % (self.env, request_id, segment_id)
        self.driver.get(url)
        return SCR0115(self.driver)

    def get_document_count(self):
        count = self.find_element(locators["document count"]).text
        return count[:count.find(" ")]

    def goto_research_team(self):
        self.find_element(locators["research staff"]).click()
        from pages.SCR0015 import SCR0015
        return SCR0015(self.driver)

    def initiate_review(self):
        self.find("initiate review").click()
        return self.load_page()

    def submit(self):
        self.find("submit").click()
        return self.load_page()

    def log_notice(self):
        return self.go("log notice")

    def edit_budget(self):
        return self.go("edit budget")
