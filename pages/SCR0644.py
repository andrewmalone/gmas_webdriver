from pages.Page import Page


class SCR0644(Page):
    """
    SCR_0644 COI Approval
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
