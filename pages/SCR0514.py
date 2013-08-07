from pages.Page import Page
from pages.elements import Text, Select


class SCR0514(Page):
    """
    SCR_0514 Add/edit person phone number
    """
    locators = {
        "type": "name=phoneTypeId",
        "phone": "name=phoneNumber",
        "ok": "name=AddEditPersonPhoneNumberOKEvent"
    }

    phone_type = Select("type", "Phone number type (dropdown)")
    phone = Text("phone", "Phone number (text)")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0025 or SCR_0252
        """
        return self.go("ok")