from pages.Page import Page


class SCR0387(Page):
    """
    SCR_0387 Associate requests to notice
    """
    locators = {
        "next": "name=IdentifyRequestsForNoticeNextEvent"
    }

    def check_first(self):
        """
        Checks the first request on the page
        """
        self.find_element("css=input[type=checkbox]").click()

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0083
        """
        return self.go("next")