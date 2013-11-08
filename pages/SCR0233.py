from pages.Page import Page
from pages.elements import Text


class SCR0233(Page):
    locators = {
        "documents": "link=Documents"        
    }

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    
