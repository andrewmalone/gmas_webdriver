from pages.Page import Page
from pages.elements import Text


class SCR0453(Page):
    """
    SCR_0453 Edit notice attributes
    """
    locators = {
        "ok": "EditNoticeAttributesOkEvent",
        "title": "noticeTitle"
    }

    title = Text("title", "Notice title")

    def ok(self):
        """
        Clicks <Ok>
        Goes to SCR_0309
        """
        return self.go("ok")
