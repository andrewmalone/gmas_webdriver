from pages.Page import Page


class SCR0612b(Page):
    locators = {
        "next": "name=CreateGrantsGovQuestionsNextEvent"
    }

    def ok(self):
        self.find("next").click()
        return self.load_page()
