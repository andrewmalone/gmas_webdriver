from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_person, Lookup_organization

class SCR0092(Page):
    """
    SCR_0092 Add subagreement in RGS
    """
    locators = {
        "sub name text": "name=subrecipientName",
        "sub pi text": "name=vendorPIName",
        "start": "name=proposedStartDate",
        "end": "name=proposedEndDate",
        "ok": "name=SubagreementDetailsOKEvent"
    }

    sub_name_text = Text("sub name text", "subagreement name text input")
    sub_name = Lookup_organization(sub_name_text, "orgLookupImage", "Subagreement organization")

    sub_pi_text = Text("sub pi text", "subagreement PI text input")
    sub_pi = Lookup_person(sub_pi_text, "vendorPILookupImage", "Subagreement PI")

    start = Text("start", "Subagreement start date")
    end = Text("end", "Subagreement end date")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0091
        """
        return self.go("ok")

