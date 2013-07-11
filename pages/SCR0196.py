from pages.Page import Page

locators = {
    "add account": "name=AddAccountRevisionEvent",
    "ok": "name=EditAccountsSaveChangesEvent",
    "edit account": "link=REPLACE"
}


class SCR0196(Page):
    locators = locators

    def add_account(self):
        self.find_element(locators["add account"]).click()
        from pages.SCR0474 import SCR0474
        return SCR0474(self.driver)

    def ok(self):
        self.find_element(locators["ok"]).click()
        from pages.SCR0105 import SCR0105
        return SCR0105(self.driver)

    def edit_account(self, account_name):
        self.find("edit account", account_name).click()
        from pages.SCR0474 import SCR0474
        return SCR0474(self.driver)
