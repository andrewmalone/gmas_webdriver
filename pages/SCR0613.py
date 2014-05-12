from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_opportunity


class SCR0613(Page):
    """
    SCR_0613 Opportunity search
    """
    locators = {
        "opportunity": "name=opportunity_id",
        "validate": "css=img[alt='Validate']",
        "next": "name=EnterOpportunityNextEvent",
        "cancel": "EnterOpportunityCancelEvent"
    }

    opportunity_text = Text("opportunity", "opportunity number text box")
    opportunity = Lookup_opportunity(opportunity_text, "opportunityNumberImage", "Opportunity lookup")
    # override the default lookup since it isn't standard
    opportunity.lookup_locator = locators["validate"]

    def ok(self):
        """
        Clicks <Next>
        Goes to SCR_0231 or SCR_0231b
        """
        return self.go("next")

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")
