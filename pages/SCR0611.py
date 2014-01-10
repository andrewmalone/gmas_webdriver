# @todo - change file to use element.File
from pages.Page import Page


class SCR0611(Page):
    """
    SCR_0611 Add Grants.gov attachment
    """
    locators = {
        "ok": "css=img[src$='b_ok.gif']",
        "file": "name=file1"
    }

    def set_file(self, file_location):
        """
        Set the location of the file to upload.

        This needs to be a local path with double backslashes
        Example: "C:\\Users\\apm228\\Documents\\test.pdf"
        """
        self.find("file").send_keys(file_location)

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0610b
        """
        self.find("ok").click()
        self.w.until(lambda p: p.find_element_by_css_selector("input[name='formName'][value='GrantsGovAttachmentsForm']"))
        return self.load_page()