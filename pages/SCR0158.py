from pages.Page import Page

class Document_row(object):
    # expects to be passed a table row...
    def __init__(self, row, page):
        # need to check for exception here?
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.checkbox = row.find_element_by_css_selector("input[type='checkbox']")
        except NoSuchElementException:
            self.checkbox = None
        self.link = row.find_element_by_css_selector("a[href*='DocumentFolderFilesLinkEvent']")
        self.name = self.link.text
        #self.type = row.find_elements_by_tag_name("td")[12].text
        #self.status = row.find_elements_by_tag_name("td")[24].text
        self.page = page

    def check(self):
        if self.checkbox != None and self.checkbox.get_attribute("checked") != "true":
            self.checkbox.click()

    def uncheck(self):
        if self.checkbox != None and self.checkbox.get_attribute("checked") == "true":
            self.checkbox.click()

    def go(self):
        self.link.click()
        return self.page.load_page()


class SCR0158(Page):
    """
    SCR_0158 Move document from clipboard
    """
    locators = {
	"doc link": "css=a[href*='DocumentFolderFilesLinkEvent']",
	"ok": "name=MoveFromMyFileCabinetOkEvent",
    "document row": "xpath=//a[contains(@href,'DocumentFolderFilesLinkEvent')]/../..",
    "document row by name": "xpath=//a[normalize-space(text())='REPLACE']/../.."
    }

    def document(self, identifier):
        """
        returns a document row object from the page based on an identifier, which can be a number or a string. If a string is passed, it returns the row with that document name (exact match). If a number is passed, it returns that number row from the list. For example, {{p.document(2)}} will return the second document on the page.

        The returned object contains the following attributes and methods:
        * *name* - The name of the document (File name column on the screen)
        * *type* - The type of document ("Document" or "Email")
        * *status* - Document status ("Checked in", "Locked", "Read only", etc,)
        * *check()* - Checks the box next to the document
        * *uncheck()* - Unchecks the box next to the document
        * *go()* - Clicks the link to go to the detail page. Goes to SCR_0135

        *Example:* To check the box next to the third document on the page, do {{p.document(3).check()}}
        """
        if type(identifier) is int:
            row = self.finds("document row")[identifier - 1]
            return Document_row(row, self)
        if type(identifier) is str:
            row = self.find("document row by name", identifier)
            return Document_row(row, self)

    def goto_first_doc(self):
        return self.go("doc link")

    def ok(self):
        """
        Clicks <Ok>
        Stays on SCR0037
        """
        return self.go("ok")

    