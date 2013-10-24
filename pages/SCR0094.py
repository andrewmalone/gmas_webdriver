from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_org, Lookup_person

class SCR0094(Page):
    """
    SCR_0094 Add new IFI in RGS
    """
    locators = {
        "org": "name=orgDescription",
        "pi": "name=personName",
        "start": "name=involvementStartDate",
        "end": "name=involvementEndDate",
        "ok": "name=MultiTubMultiOrgOKEvent"
    }

    org_text = Text("org", "Input box for the Org")
    pi_text = Text("pi", "Input box for the IFI PI")
    start = Text("start", "IFI start date")
    end = Text("end", "IFI end date")
    org = Lookup_org(org_text, "picture", "IFI Org")
    pi = Lookup_person(pi_text, "piImage" "IFI PI")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0228
        """
        return self.go("ok")