from pages.Page import Page



class SCR0134a(Page):
    """
    SCR_01134a Organization Profile
    """
    locators = {
        "documents": "event=RepositoryLinkEvent"     
    }

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    
