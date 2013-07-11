from pages.Page import Page


class SCR0387(Page):
    locators = {
        "next": "name=IdentifyRequestsForNoticeNextEvent"
    }

    def check_first(self):
        self.find_element("css=input[type=checkbox]").click()

    def ok(self):
        self.find("next").click()
        return self.load_page()