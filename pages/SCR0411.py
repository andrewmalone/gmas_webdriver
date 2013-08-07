from pages.Page import Page
from pages.elements import Text, Select


class SCR0411(Page):
    """
    SCR_0411 Add/edit person address
    """
    locators = {
        "line1": "name=addressLine1",
        "city": "name=city",
        "state": "name=stateProvinceId",
        "zip": "name=zipCode",
        "ok": "name=AddEditPersonAddressOKEvent"
    }

    line1 = Text("line1", "Address line 1 (text)")
    city = Text("city", "City (text)")
    state = Select("state", "State (dropdown)")
    zip_code = Text("zip", "Zip code (text)")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0025 or SCR_0252
        """
        return self.go("ok")