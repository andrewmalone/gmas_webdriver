from pages.Page import Page


class SCR0300(Page):
    """
    SCR_0300 Admin team
    """
    locators = {
        "role": "link=REPLACE"
    }

    def goto_role(self, role):
        """
        Clicks the first matching role link (exact match)
        Goes to SCR_0301
        """
        return self.go("role", role)