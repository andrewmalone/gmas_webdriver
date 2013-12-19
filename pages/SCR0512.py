from pages.Page import Page


class SCR0512(Page):
    locators = {
        "next": "name=ContinuationPeriodConfirmationNextEvent"
    }

    def ok(self):
        return self.go("next")