from pages.Page import Page
from pages.elements import RText
import utilities.xpath as xpath

class SCR0618(Page):
    """
    SCR_0618
    """
    locators = {
        "update": "GrantsGovSubmissionHistoryGetUpdateEvent",
        "tracking": "xpath=%s" % xpath.xpath_text_sibling("td", "Grants.gov tracking no.", 2),
        "status": "xpath=%s" % xpath.xpath_text_sibling("td", "Submission status", 2)
    }

    tracking = RText("tracking", "Grants.gov tracking number")
    status = RText("status", "Grants.gov status")