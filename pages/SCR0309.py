from pages.Page import Page


class SCR0309(Page):
    """
    SCR_0309 Notice Home
    """
    locators = {
        "review completed": "name=ReviewCompletedEvent",
        "revise project": "name=CreateNewRevisionEvent",
        "documents": "link=Documents"
    }

    def review_completed(self):
        return self.go("review completed")

    def revise_project(self):
        return self.go("revise project")

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")
