from pages.Page import Page
from pages.elements import Text, Select, Radio


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
        "foreign": "css=input[name='foreignCurrencyFlag']"
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
    arra = Radio("arra", "ARRA funding?")
    ia = Radio("ia", "Institutional authorities")
    snap = Radio("snap", "SNAP")
    equipment = Radio("equipment", "Special equipment terms")
    agency = Radio("agency", "Agency fund")
    foreign = Radio("foreign", "Foreign curency flag")

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
        
