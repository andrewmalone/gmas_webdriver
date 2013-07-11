from pages.Page import Page

class SCR0377(Page):
    locators = {
        "finish": "name=NoticeRecordConfirmationFinishEvent"
    }

    def ok(self):
        self.find("finish").click()
        return self.load_page()