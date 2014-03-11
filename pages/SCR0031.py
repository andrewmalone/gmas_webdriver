from pages.Page import Page


class SCR0031(Page):
    """
    SCR_0031 View proposal budget
    """
    locators = {
        "edit": "ViewProposedBudgetEditPostsubmissionEvent",
        "indirect": "event=ViewProposedBudgetViewIndirectCostRateEvent",
        "modular": "event=ViewProposedBudgetViewModularBudgetEvent"
    }

    def edit(self):
        """
        Click the <Edit proposal budget> button
        Goes to SCR_0006 (for initial/competing)
        """
        return self.go("edit")

    def goto_indirect(self):
        """
        Click "Total indirect costs"
        Goes to SCR_0410
        """
        return self.go("indirect")

    def goto_modular(self):
        """
        Click "View modular budget"
        Goes to SCR_0438
        """
        return self.go("modular")

    def has_modular(self):
        """
        Returns True/False depending on if there is a modular budget link
        """
        if len(self.finds("modular")) == 0:
            return False
        else:
            return True

