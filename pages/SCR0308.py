from pages.Page import Page


class SCR0308(Page):
    locators = {
        "log notice": "name=LogNoticeEvent"
    }

    def log_notice(self):
        self.find("log notice").click()
        return self.load_page()