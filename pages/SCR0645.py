from pages.Page import Page


class SCR0645(Page):
    locators = {
        "ok": "name=ConfirmResearchTeamOkEvent"
    }

    def ok(self):
        # to segment home
        return self.go("ok")