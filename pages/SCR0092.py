from pages.Page import Page
from pages.elements import Text, Row, Select
from pages.lookups import Lookup_person, Lookup_organization


class SCR0092(Page):
    """
    SCR_0092 Add subagreement in RGS
    """
    locators = {
        "sub name text": "name=subrecipientName",
        "sub pi text": "name=vendorPIName",
        "admin text": "vendorAdminName",
        "start": "name=proposedStartDate",
        "end": "name=proposedEndDate",
        "ok": "name=SubagreementDetailsOKEvent",
        "description": "description",
        "rate": "xpath=//input[contains(@name, 'idcRateVersion')]//ancestor::tr[1]",
        "add rate": "RequestAddSubrecipientRateEvent",
        "basis": "indirectBasisTypeId"
    }

    sub_name_text = Text("sub name text", "subagreement name")
    sub_name = Lookup_organization(sub_name_text, "orgLookupImage", "Subagreement organization")

    sub_pi_text = Text("sub pi text", "subagreement PI")
    sub_pi = Lookup_person(sub_pi_text, "vendorPILookupImage", "Subagreement PI")

    sub_admin_text = Text("admin text", "Sub admin contact")
    sub_admin = Lookup_person(sub_admin_text, "administratorImage", "Sub admin contact")

    start = Text("start", "Subagreement start date")
    end = Text("end", "Subagreement end date")

    description = Text("description", "Description")
    basis = Select("basis", "Indirect basis")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0091
        """
        return self.go("ok")

    def rate(self, n):
        """
        Nth Sub IDC rate rows
        """
        row = self.finds("rate")[n - 1]
        return self.Rate_row(row, self)

    def add_rate(self):
        """
        Click <Add rate>
        """
        return self.go("add rate")

    class Rate_row(Row):
        locators = {
            "rate": "css=input[type=text][name^=rate]",
            "date": "css=input[type=text][name^=expirationDate]"
        }

        rate = Text("rate", "Indirect rate")
        expiration = Text("date", "Indirect expiration")

