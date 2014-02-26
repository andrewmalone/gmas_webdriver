from pages.Page import Page


class SCR0031(Page):
    """
    SCR_0031 View proposal budget
    """
    locators = {
        "edit": "ViewProposedBudgetEditPostsubmissionEvent"
    }

    def edit(self):
        """
        Click the <Edit proposal budget> button
        Goes to SCR_0006 (for initial/competing)
        """
        return self.go("edit")