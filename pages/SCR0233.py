from pages.Page import Page


class SCR0233(Page):
    """
    SCR_0233 Subagreement home
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