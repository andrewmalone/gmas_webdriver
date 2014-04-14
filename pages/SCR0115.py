from pages.Page import Page
import utilities.xpath as xpath
from pages.elements import RText


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
        "view ggov questions": "event=ViewGrantsGovQuestionsEvent",
        "edit ggov attachments": "css=a[href*='EditGrantsGovAttachmentsEvent'] img",
        "view ggov attachments": "event=ViewGrantsGovAttachmentsEvent",
        "prepare ggov submission": "css=a[href*='PrepareGrantsGovSubmissionEvent'] img",
        "edit atrisk": "css=a[href*='AtRiskAccountEditEvent'] img",
        "budget": "event=ProposedDollarsSummaryViewBudgetEvent",
        "subagreements": "event=ViewListOfSubagreementsEvent",
        "submissions": "event=RequestSubmissionSummaryLinkEvent",
        "status": xpath.text_sibling("td", "Status", 2),
        "preview": "event=GrantsGovPreviewLinkEvent"
        "r2r": "event=ReviseThisRequestEvent",
    }

    status = RText("status", "Request status")

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

    def r2r(self):
        """
        Click <Revise to resubmit>
        Goes to SCR_0409
        """
        return self.go("r2r")

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

    def goto_attachments(self):
        """
        Click the "Grants.gov attachments" link
        Goes to SCR_0610c
        """
        return self.go("view ggov attachments")

    def edit_questions(self):
        """
        Click <edit> in the ggov questions component
        Goes to SCR_0612b
        """
        return self.go("edit ggov questions")

    def goto_questions(self):
        """
        Click the "Grants.gov questions link
        Goes to SCR_0612c
        """
        return self.go("view ggov questions")

    def prepare_ggov_submission(self):
        """
        Click <Prepare Grants.gov submission>
        Goes to SCR_0609
        """
        return self.go("prepare ggov submission")

    def edit_atrisk(self):
        """
        Click <edit> for at-risk
        Goes to SCR_0378
        """
        return self.go("edit atrisk")

    def goto_budget(self):
        """
        Click the "Budget" link
        Goes to SCR_0031
        """
        return self.go("budget")

    def goto_subagreements(self):
        """
        Click the "Subagreement" link
        Goes to SCR_0250
        """
        return self.go("subagreements")

    def goto_submissions(self):
        """
        Click "Submissions"
        Goes to SCR_0406
        """
        return self.go("submissions")

    def goto_preview(self):
        """
        Click "Preview"
        Goes to SCR_0615a
        """
        return self.go("preview")
