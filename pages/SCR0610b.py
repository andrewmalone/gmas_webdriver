from pages.Page import Page


class SCR0610b(Page):
    """
    SCR_0610b Grants.gov attachments (RGS)
    """
    locators = {
        "next": "name=GrantsGovAttachmentsNextEvent"
    }

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0332
        """
        self.find("next").click()
        return self.load_page()
