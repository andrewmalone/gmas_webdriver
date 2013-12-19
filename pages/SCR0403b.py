from pages.Page import Page


class SCR0403b(Page):
    locators = {
        "next": "name=EditApprovalAttributesNextEvent"
    }

    def next(self):
        return self.go("next")