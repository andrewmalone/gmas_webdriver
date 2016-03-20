from pages.Page import Page
from pages.elements import Text, Select, Radio
from pages.lookups import Lookup_org, Lookup_person


class SCR0328(Page):
    """
    SCR_0328 Award identifying information
    """
    locators = {
        "ok": "name=EditSegmentRevisionAwardInformationDoneEvent",
        "next": "name=EditSegmentRevisionAwardInformationNextEvent",
        "funding instrument": "name=fundingInstrument",
        "payment method": "name=paymentMethodId",
        "loc": "name=agencyLOCNumber",
        "cfda": "name=cfdaNumber",
        "arra": "css=input[name='arraFundingFlag']",
        "ia": "css=input[name='expandedAuthorityFlag']",
        "snap": "css=input[name='snapFlag']",
        "equipment": "css=input[name='specialEquipmentTermsFlag']",
        "agency": "css=input[name='agencyFundFlag']",
        "foreign": "css=input[name='foreignCurrencyFlag']",
        "prime": "primeAwardNumber",
        "org text": "orgDescriptor",
        "pi text": "pI",
        "mentor text": "fellow",
        "title": "title",
        "award number": "css=input[name$=awardNumber]",
        "discipline": "disciplineId",
        "ug": "css=input[name='uniformGuidanceFlag']"
    }

    funding_instrument = Select("funding instrument", "Funding instrument", docextra="""
        * Grant
        * Contract
        * Cooperative agreement
        """)
    payment_method = Select("payment method", "Payment method", docextra="""
        * ACH
        * Check
        * EFT
        * Letter Of Credit
        * RSO Advice
        * Wire
        """)
    loc_number = Text("loc", "Agency LOC number")
    cfda = Text("cfda", "CFDA number")
    ug = Radio("ug", "Uniform Guidance")
    arra = Radio("arra", "ARRA funding?")
    ia = Radio("ia", "Institutional authorities")
    snap = Radio("snap", "SNAP")
    equipment = Radio("equipment", "Special equipment terms")
    agency = Radio("agency", "Agency fund")
    foreign = Radio("foreign", "Foreign curency flag")
    prime = Text("prime", "Prime award number")
    org_text = Text("org text", "Input box for Org")
    org = Lookup_org(org_text, "orgLookupImage", "Org lookup")
    pi_text = Text("pi text", "Input box for PI")
    pi = Lookup_person(pi_text, "pILookupImage", "PI lookup")
    mentor_text = Text("mentor text", "Input box for Mentor")
    mentor = Lookup_person(mentor_text, "fellowLookupImage", "Mentor lookup")
    award_number = Text("award number", "Award number - currently only works for the top award number")
    discipline = Select("discipline", "Disclipline")
    title = Text("title", "Project title")

    def ok(self):
        """
        Click <Done making revisions to this section
        Goes to SCR_0105
        """
        return self.go("ok")

    def next(self):
        """
        Click <Next>
        Goes to SCR_0324
        """
        return self.go("next")
        
