from pages.Page import Page
from pages.elements import Text

class SCR0137(Page):
     """
     SCR_0137 Rename document
     """
     locators = {
        "new_name": "name=newName",
        "ok": "name=RenameDocumentOkEvent"
     }

     new_name = Text("new_name", "Text entry for new name")

     def ok(self):
        """
        Clicks <Ok>
        Goes to SCR_0135
        """
        return self.go("ok")
