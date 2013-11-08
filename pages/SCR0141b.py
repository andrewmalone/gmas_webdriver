from pages.Page import Page
from pages.elements import Text

class SCR0141b(Page):
    """
    SCR_0141b document edit description
    """
    locators = {
        "description": "name=documentDescription",
        "ok": "name=EditDocumentOkEvent"
    }


    description = Text("description", "Textarea for description")
    

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0135
        """
        return self.go("ok")