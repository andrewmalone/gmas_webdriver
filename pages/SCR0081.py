from pages.Page import Page


class SCR0081(Page):
    """
    SCR_0081 Edit Approval
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

    
