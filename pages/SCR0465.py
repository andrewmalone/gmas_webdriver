from pages.Page import Page
from pages.elements import Text


class SCR0465(Page):
    """
    SCR_0465 Edit request justification
    """
    locators = {
        "justification": "name=requestJustification",
        "ok": "name=EditJustificationOKEvent"
    }

    justification = Text("justification", "Text box for justification")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0115
        """
        return self.go("ok")