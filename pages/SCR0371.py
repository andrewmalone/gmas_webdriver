from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_person


class SCR0371(Page):
    """
    SCR_0371 Log signature
    """
    locators = {
        "date": "dateSigned",
        "ok": "LogSignatureOKEvent",
        "name text": "personName"
    }

    name_text = Text("name text", "Signatory name edit field")
    name = Lookup_person(name_text, "piImage", "Signatory name")
    date = Text("date", "Date signed")

    def ok(self):
        """
        Click <Ok>
        Goes to referring screen (SCR_0115)
        """
        return self.go("ok")
