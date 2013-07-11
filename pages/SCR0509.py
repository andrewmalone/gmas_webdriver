from pages.Page import Page


class SCR0509(Page):
    locators = {
        "next": "name=ConfirmRequiredSignaturesNextEvent"
    }

    def ok(self):
        self.find("next").click()
        return self.load_page()
