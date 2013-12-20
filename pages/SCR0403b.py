from pages.Page import Page


class SCR0403b(Page):
    """
    SCR_0403b Edit approval attributes in revision
    """
    locators = {
        "next": "name=EditApprovalAttributesNextEvent"
    }

    def next(self):
        """
        Click <Next>
        Goes to SCR_0359
        """
        return self.go("next")