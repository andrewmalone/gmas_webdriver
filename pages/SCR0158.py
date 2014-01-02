from pages.Page import Page
from pages.elements import Row, Checkbox


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
        returns a document row object from the page based on an identifier, which can be a number or a string.
        If a string is passed, it returns the row with that document name (exact match).
        If a number is passed, it returns that number row from the list.
        For example, `p.document(2)` will return the second document on the page.
        //Document_row
        *Example:* To check the box next to the third document on the page, do `p.document(3).check()`
        """
        if type(identifier) is int:
            row = self.finds("document row")[identifier - 1]
            
        if type(identifier) is str:
            row = self.find("document row by name", identifier)

        return self.Document_row(row, self)

    def goto_first_doc(self):
        """
        Clicks the link for the first document on the page
        Goes to SCR_0135

        **DEPRECATED**: Use `p.document(1).go()` syntax instead
        """
        print "goto_first_doc() is deprecated. Use p.document(1).go() instead"
        return self.go("doc link")

    def ok(self):
        """
        Clicks <Ok>
        Goes to SCR_0433
        """
        return self.go("ok")

    class Document_row(Row):
        locators = {
            "checkbox": "css=input[type='checkbox']",
            "link": "css=a[href*='DocumentFolderFilesLinkEvent']"
        }

        checkbox = Checkbox("checkbox", "Checkbox to select document")

        def check(self):
            """
            Checks the box next to the document
            """
            self.checkbox = True

        def uncheck(self):
            """
            Unchecks the box next to the document
            """
            self.checkbox = False

        def go(self):
            """
            Clicks the document link
            Goes to SCR_0135
            """
            return self._go("link")