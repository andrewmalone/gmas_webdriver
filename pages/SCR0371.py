from pages.Page import Page
from pages.elements import Text


class SCR0371(Page):
    """
    SCR_0371 Log signature
    """
    locators = {
        "date": "dateSigned",
        "ok": "LogSignatureOKEvent"
    }

    date = Text("date", "Date signed")

    def ok(self):
        """
        Click <Ok>
        Goes to referring screen (SCR_0115)
        """
        return self.go("ok")
