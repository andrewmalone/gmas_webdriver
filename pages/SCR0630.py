from pages.Page import Page


class SCR0630(Page):
    """
    SCR_0630 LOC Home
    """	
    locators = {
        "documents": "link=Documents"
    }

    
    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")
    
