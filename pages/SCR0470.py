from pages.Page import Page
from pages.elements import Text


class SCR0470(Page):
    """
    SCR_0470 Add/edit person email
    """
    locators = {
        "email": "name=emailAddress",
        "ok": "name=AddEditPersonEmailAddressOKEvent"
    }

    email = Text("email", "Email address (text)")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0025 or SCR_0252
        """
        return self.go("ok")