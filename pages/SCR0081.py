from pages.Page import Page


class SCR0081(Page):
    """
    SCR_0081 Edit Approval
    """
    locators = {
        "documents": "event=RepositoryLinkEvent",
        "cancel": "ApprovalEditCancelEvent"
    }

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def cancel(self):
        """
        Clicks the <Cancel> button
        Goes to SCR_0080
        """
        return self.go("cancel")
