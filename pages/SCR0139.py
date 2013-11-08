from pages.Page import Page


class SCR0139(Page):
    """
    SCR_0139 User document clipboard
    """
    locators = {
    	"add document": "name=MyFileDocumentAddDocumentEvent"        
    }

    def add_document(self):
        """
        Click the <Add document> button
        Goes to SCR_0141a
        """
        return self.go("add document")

    
