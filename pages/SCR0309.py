from pages.Page import Page


class SCR0309(Page):
    """
    SCR_0309 Notice Home
    """
    locators = {
        "review completed": "ReviewCompletedEvent",
        "revise project": "CreateNewRevisionEvent",
        "documents": "link=Documents",
        "status": "xpath=//td[contains(text(), 'Notice status')]",
        "edit_attributes": "EditNoticeAttributesEvent"
    }

    @property
    def notice_status(self):
        """
        Status as displayed on the screen
        """
        return self.find("status").text.replace("Notice status: ", "")

    def review_completed(self):
        """
        Click <Review completed>
        Stays on SCR_0309
        """
        return self.go("review completed")

    def revise_project(self):
        """
        Click <Revise project based on this notice>
        Goes to SCR_0328
        """
        return self.go("revise project")

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def edit_attributes(self):
        """
        Clicks the <Edit notice attributes> button
        Goes to SCR_0453
        """
        return self.go("edit_attributes")
