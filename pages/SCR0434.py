from pages.Page import Page
from pages.elements import Text

class SCR0434(Page):
    """
    SCR_0434 Create folder
    """
    locators = {
        "folder_name": "name=repositoryName",
        "ok": "name=CreateFolderOkEvent"
    }

    folder_name = Text("folder_name", "Text entry for folder name")

    def ok(self):
        """
        Clicks <Ok>
        Goes to SCR_0433
        """
        return self.go("ok")
