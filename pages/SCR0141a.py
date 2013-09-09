from pages.Page import Page
from pages.elements import Text, Checkbox, File

class SCR0141a(Page):
    """
    SCR_0141a document upload
    """
    locators = {
        "file": "name=file1",
        "description": "name=MasterDescription",
        "readonly": "name=readOnly",
        "ok": "css=input[value='OK']"
    }

    filename = File("file", """
        File path to upload (full local path with double backslashes)
        example: p.file = "C:\\\\Users\\\\apm228\\\\Documents\\\\test.pdf"
        """)
    description = Text("description", "Textarea for description")
    readonly = Checkbox("readonly", "Readonly checkbox (set to True or False)")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0433
        """
        self.find("ok").click()
        self.w.until(lambda p: p.find_element_by_css_selector("input[name='formName'][value='DocumentFileForm']"))
        return self.load_page()