from pages.Page import Page


class SCR0487(Page):
    """
    SCR_0487 Confirm Initiate Review
    """
    locators = {
        "finish": "name=ConfirmInitiateReviewOKEvent"
    }

    def ok(self):
        """
        Click <Finish>
        Goes to SCR_0115
        """
        return self.go("finish")
