from pages.Page import Page


class SCR0487(Page):
    locators = {
        "finish": "name=ConfirmInitiateReviewOKEvent"
    }

    def ok(self):
        self.find("finish").click()
        return self.load_page()
