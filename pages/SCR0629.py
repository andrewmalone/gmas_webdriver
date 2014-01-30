from pages.Page import Page
from pages.elements import Select, Text

class SCR0629(Page):
    """
    SCR_0629 Add/edit agency credentials
    """
    locators = {
        "agency": "agencyId",
        "credential": "credential",
        "ok": "AddEditPersonCredentialOKEvent"
    }

    agency = Select("agency", mapping={
            "DOD": "DOD/CDMRP",
            "NIH": "eRACommons",
            "NSF": "NSF"
        })
    credential = Text("credential", "Agency credential")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0025
        """
        return self.go("ok")