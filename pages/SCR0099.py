from pages.Page import Page


class SCR0099(Page):
    locators = {
        "next": "name=GrantsMgmtStaffNextEvent"
    }

    def ok(self):
        self.find("next").click()
        return self.load_page()
