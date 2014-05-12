from pages.Page import Page
from pages.elements import Text, Select, Radio
from pages.lookups import Lookup_org


class SCR0088(Page):
    """
    SCR_0088 (Initial proposal instructions)
    """
    locators = {
        "select project type": "name=researchTypeId",
        "org input": "name=org",
        "retro": "css=input[name='isRetroactiveRequest'][value='REPLACE']",
        "next": "name=InitialProposalInstructionsNextEvent",
        "cancel": "InitialProposalInstructionsCancelEvent"
    }

    project_type = Select("select project type", "Project type dropdown")
    org_text = Text("org input", "Text box for org lookup")
    org = Lookup_org(org_text, "picture")
    retro = Radio("retro", "Retroactive yes/no question - set to true/false")

    def ok(self):
        """
        Clicks the <Next> button
        Goes to SCR_0089
        """
        return self.go("next")

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")
