from pages.Page import Page


class SCR0080(Page):
    """
    SCR_0080 Approval List
    """
    locators = {
        "approval link": "css=a[href*='ApprovalListViewOrEditDetailEvent']"        
    }

    def goto_first_approval(self):
        """
        Click the first approval in the list
        """
        # TODO - document which pages here
        return self.go("approval link")