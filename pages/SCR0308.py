from pages.Page import Page


class SCR0308(Page):
    locators = {
        "log notice": "name=LogNoticeEvent",
        "notice link": "css=a[href*='ViewDetailsOfNoticeEvent']"
    }

    def log_notice(self):
        self.find("log notice").click()
        return self.load_page()

    def goto_first_notice(self):
        return self.go("notice link")