from pages.Page import Page
from pages.elements import Text, File

class SCR0138(Page):
    """
    SCR_0138 Checkin Document
    """
    locators = {
        "file": "name=file1",
        "description": "name=versionDescription",
        "ok": "css=input[value='OK']"
    }

    filename = File("file", """
        File path to upload (full local path with double backslashes)
        example: p.file = "C:\\\\Users\\\\apm228\\\\Documents\\\\test.pdf"
        """)
    description = Text("description", "Textarea for description")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0135
        """
        return self.go("ok")