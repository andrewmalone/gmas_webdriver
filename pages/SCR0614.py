from pages.Page import Page


class SCR0614(Page):
    locators = {
        "ok": "name=OpportunityValidationResultEvent"
    }

    def ok(self):
        self.find("ok").click()
        self.driver.switch_to_window(self.driver.window_handles[0])