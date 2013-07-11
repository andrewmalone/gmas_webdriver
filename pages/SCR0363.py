from pages.Page import Page


class SCR0363(Page):
    locators = {
        "edit personnel": "name=EditPersonnelEvent"
    }

    def edit_personnel(self):
        self.find("edit personnel").click()
        return self.load_page()
