from pages.Page import Page


class SCR0426(Page):
    """
    SCR_0426 Segment revision detail
    """
    locators = {
        "open_all": "link=open all"
    }

    def open_all(self):
        """
        Click "open all"
        """
        return self.go("open_all")
