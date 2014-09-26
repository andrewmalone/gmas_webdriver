from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_person


class SCR0400(Page):
    """
    SCR_0400 Edit request info
    """
    locators = {
        "pi_text": "piName",
        "ok": "EditInitialRequestInfoOKEvent"
    }

    pi_text = Text("pi_text", "Edit box for PI name")
    pi = Lookup_person(pi_text, "piImage", "PI Lookup")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0115
        """
        return self.go("ok")
