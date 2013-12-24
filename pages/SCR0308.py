from pages.Page import Page


class SCR0308(Page):
    """
    SCR_0308 Notice list
    """
    locators = {
        "log notice": "name=LogNoticeEvent",
        "notice link": "css=a[href*='ViewDetailsOfNoticeEvent']"
    }

    def log_notice(self):
        """
        Click <Log notice>
        Goes to SCR_0387
        """
        return self.go("log notice")

    def goto_first_notice(self):
        """
        Click the first notice on the page
        Goes to SCR_0309
        """
        return self.go("notice link")