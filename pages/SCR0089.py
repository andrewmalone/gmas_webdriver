#testing git workflows

from pages.Page import Page
from pages.elements import Text, Select, Radio
from pages.lookups import Lookup_person, Lookup_organization


class SCR0089(Page):
    """
    SCR_0089
    """
    locators = {
        "title": "name=requestTitle",
        "sponsor": "name=sponsor",
        "prime sponsor": "name=primeSponsor",
        "pi": "name=piName",
        "mentor": "name=mentorInvestigatorName",
        "prime pi": "name=primePiName",
        "A21": "name=a21functionalId",
        "discipline": "name=disciplineId",
        "rfp": "css=input[name='isInResponseToRFP'][value='REPLACE']",
        "subs": "css=input[name='hasSubAgreements'][value='REPLACE']",
        "ifi": "css=input[name='isOtherSchoolSharing'][value='REPLACE']",
        "comment": None,
        "cancel": None,
        "back": None,
        "next": "name=CreateInitialRequestNextEvent"
    }
    title = Text("title", "Project title")
    sponsor_text = Text("sponsor", "Sponsor name text input")
    sponsor = Lookup_organization(sponsor_text, "sponsorValidatedImage", "Sponsor lookup")
    prime_sponsor_text = Text("prime sponsor", "Prime sponsor name text input")
    prime_sponsor = Lookup_organization(prime_sponsor_text, "primeSponsorValidatedImage", "Prime sponsor lookup")
    pi_text = Text("pi", "PI name text input box")
    pi = Lookup_person(pi_text, "piImage", "PI lookup")
    mentor_text = Text("mentor", "Mentor name text input box")
    mentor = Lookup_person(mentor_text, "mentorValidatedImage", "Mentor lookup")
    prime_pi_text = Text("prime pi", "Prime PI name text input box")
    prime_pi = Lookup_person(prime_pi_text, "primePiImage", "Prime PI lookup")
    a21 = Select("A21", "A21 dropdown")
    discipline = Select("discipline", "Discipline dropdown")
    rfp = Radio("rfp", "RFP question radio button (true/false)")
    subs = Radio("subs", "Subagreement question radio button (true/false)")
    ifi = Radio("ifi", "IFI radio button question (true/false)")

    def ok(self):
        """
        Clicks the <Ok> button
        Goes to SCR_0613 or SCR_0231
        """
        self.find("next").click()
        return self.load_page()
