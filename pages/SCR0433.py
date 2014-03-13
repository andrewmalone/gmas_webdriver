from pages.Page import Page
from pages.elements import Row, Checkbox, RText


class SCR0433(Page):
    """
    SCR_0433 Document list
    """
    locators = {
        "add document": "name=DocumentFolderAddADocumentEvent",
        "add folder": "name=DocumentFolderAddAFolderEvent",
        "document row": "xpath=//a[contains(@href,'DocumentFolderFilesLinkEvent')]/../..",
        "document row by name": "xpath=//a[normalize-space(text())='REPLACE'][not(@class)]/../..",
        "delete": "name=DocumentFolderDeleteDocumentEvent",
        "lock": "name=DocumentFolderLockDocumentEvent",
        "get from clipboard": "name=DocumentFolderGetFromMyClipboardEvent",
        "move to clipboard": "name=DocumentFolderMoveSelectedToMyClipboardEvent",
        "folder row": "xpath=//a[contains(@href,'DocumentFolderLinkEvent')]/../..",
        "folder row by name": "xpath=//a[normalize-space(text())='REPLACE']/../..",
    }

    def add_document(self):
        """
        Click the <Add document> button
        Goes to SCR_0141a
        """
        return self.go("add document")

    def add_folder(self):
        """
        Click the <Add folder> button
        Goes to SCR_0434
        """
        return self.go("add folder")

    def document(self, identifier):
        """
        returns a document row object from the page based on an identifier, which can be a number or a string.
        If a string is passed, it returns the row with that document name (exact match). 
        If a number is passed, it returns that number row from the list. For example, `p.document(2)` will return the second document on the page.
        //Document_row

        **Example:** To check the box next to the third document on the page, do `p.document(3).check()`
        """
        if type(identifier) is int:
            row = self.finds("document row")[identifier - 1]
            
        if type(identifier) is str:
            row = self.find("document row by name", identifier)

        return self.Document_row(row, self)

    def folder(self, identifier):
        """
        returns a folder row object from the page based on an identifier, which can be a number or a string.
        If a string is passed, it returns the row with that folder name (exact match). 
        If a number is passed, it returns that number row from the list.
        //Folder_row
        
        For example, `p.folder(2)` will return the second folder on the page.
        """
        if type(identifier) is int:
            row = self.finds("folder row")[identifier - 1]
            
        if type(identifier) is str:
            row = self.find("folder row by name", identifier)

        return self.Folder_row(row, self)

    def delete(self):
        """
        Press the <Delete document> button
        Goes to SCR_0136
        """
        return self.go("delete")

    def lock(self):
        """
        Press the <Lock document> button
        """
        return self.go("lock")

    def count_documents(self):
        """
        Return the count of documents in this specific folder
        """
        return len(self.finds("document row"))

    def get_doc(self):
        """
        Get a file or email from user's clipboard
        """
        return self.go("get from clipboard")

    def move_doc(self):
        """
        Moves doc or email to user's clipboard
        """
        return self.go("move to clipboard")

    class Document_row(Row):
        locators = {
            "link": "css=a[href*='DocumentFolderFilesLinkEvent']",
            "checkbox": "css=input[type='checkbox']",
            "type": "css=td:nth-of-type(13)",
            "status": "css=td:nth-of-type(25)"
        }

        checkbox = Checkbox("checkbox", "Checkbox for delete or move")
        name = RText("link", "File name")
        type = RText("type", "Document type ('Document' or 'Email')")
        status = RText("status", "Document status ('Checked in', 'Locked', 'Read only', etc,)")

        def go(self):
            """
            Click a document link
            Goes to SCR_0135
            """
            return self._go("link")

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

    class Folder_row(Row):
        locators = {
            "radio": "selectedRadioButton",
            "link": "css=a[href*='DocumentFolderLinkEvent']"
        }

        name = RText("link", "Folder name")

        def select(self):
            """
            Clicks the radio button for the folder
            """
            self.find("radio").click()

        def go(self):
            """
            Clicks the folder link
            Goes to SCR_0433
            """
            return self._go("link")

