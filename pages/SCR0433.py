from pages.Page import Page


class SCR0433(Page):
    """
    SCR_0433 Document list
    """
    locators = {
        "add document": "name=DocumentFolderAddADocumentEvent",
        "add folder": "DocumentFolderAddAFolderEvent"
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