from pages.Page import Page


class SCR0610b(Page):
    locators = {
        "next": "name=GrantsGovAttachmentsNextEvent"
    }

    def ok(self):
        self.find("next").click()
        return self.load_page()
