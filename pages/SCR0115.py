from pages.Page import Page


class SCR0115(Page):
    """
    SCR_0115 Request Home
    """
    locators = {
        "document count": "xpath=//div[@id='DocRepositoryComponentCCBODY']/preceding-sibling::*[1]//tr[1]/td[4]",
        "documents": "link=Documents",
        "research staff": "link=Research staff",
        "initiate review": "css=a[href*='InitiateInternalReviewEvent'] img",
        "submit": "css=a[href*='SubmitToSponsorEvent'] img",
        "log notice": "css=img[alt='Log notice']",
        "edit budget": "css=a[href*='EditProposedDollarsSummaryBudgetEvent'] img",
        "edit ggov questions": "css=a[href*='EditGrantsGovQuestionsEvent'] img",
        "edit ggov attachments": "css=a[href*='EditGrantsGovAttachmentsEvent'] img",
        "prepare ggov submission": "css=a[href*='PrepareGrantsGovSubmissionEvent'] img"
    }

    def nav_to(self, segment_id, request_id):
        """
        Direct navigation to request home given a segment id and request id
        """
        url = "https://%s.harvard.edu/gmas/request/SCR0115Request.jsp?requestId=%s&segmentId=%s" % (self.env, request_id, segment_id)
        self.driver.get(url)
        return SCR0115(self.driver)

    def get_document_count(self):
        """
        Returns the count of documents from the doc repo component
        """
        count = self.find("document count").text
        return count[:count.find(" ")]

    def goto_documents(self):
        """
        Click the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def goto_research_team(self):
        """
        Click the "research staff" link
        Goes to SCR_0015
        """
        self.find("research staff").click()
        from pages.SCR0015 import SCR0015
        return SCR0015(self.driver)

    def initiate_review(self):
        """
        Click <Lock and route for signatures>
        Goes to SCR_0509 or SCR_0609
        """
        self.find("initiate review").click()
        return self.load_page()

    def submit(self):
        """
        Click <Submit to sponsor>
        Goes to SCR_0401
        """
        self.find("submit").click()
        return self.load_page()

    def log_notice(self):
        """
        Click <Log notice>
        Goes to SCR_0387
        """
        return self.go("log notice")

    def edit_budget(self):
        """
        Click <edit> in the budget component
        Goes to SCR_0006, SCR_0493, SCR_0499, or SCR_0437
        """
        return self.go("edit budget")

    def edit_attachments(self):
        """
        Click <edit> in the ggov attachements component
        Goes to SCR_0610b
        """
        return self.go("edit ggov attachments")

    def edit_questions(self):
        """
        Click <edit> in the ggov questions component
        Goes to SCR_0612b
        """
        return self.go("edit ggov questions")

    def prepare_ggov_submission(self):
        """
        Click <Prepare Grants.gov submission>
        Goes to SCR_0609
        """
        return self.go("prepare ggov submission")
