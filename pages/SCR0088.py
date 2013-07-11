from pages.Page import Page
from pages.elements import Text, Select, Radio

locators = {
    "select project type": "name=researchTypeId",
    "org input": "name=org",
    "org lookup": "css=img[alt='Lookup']",
    "org lookup match": "css=img[name='picture'][src*='i_match.gif']",
    "retro": "css=input[name='isRetroactiveRequest'][value='REPLACE']",
    "next": "name=InitialProposalInstructionsNextEvent",
    "cancel": "InitialProposalInstructionsCancelEvent"
}


class Lookup_org(object):
    """
    Org lookup - setting this value will perform the lookup (needs the 5 digit org value)
    """
    def __set__(self, obj, val):
        obj._lookup_org(val)

    def __get__(self, obj, type=None):
        pass


class SCR0088(Page):
    """
    SCR_0088 (Initial proposal instructions)
    """

    locators = locators
    project_type = Select("select project type", "Project type dropdown")
    org_text = Text("org input", "Text box for org lookup")
    org = Lookup_org()
    retro = Radio("retro", "Retroactive yes/no question")

    def _lookup_org(self, val):
        """Lookup an org

        Looks up an org without interacting with the popup

        Args:
            val: the 5 digit org value (string)
        """
        self.org_text = val
        self.find("org lookup").click()
        self.w.until(lambda e: self.find("org lookup match"))
        return self

    def ok(self):
        """
        Clicks the <Next> button
        Goes to SCR_0089abc
        """
        self.find("next").click()
        from pages.SCR0089 import SCR0089
        return SCR0089(self.driver)
