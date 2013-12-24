from pages.Page import Page


class SCR0377(Page):
    """
    SCR_0377 Finish logging notice
    """
    locators = {
        "finish": "name=NoticeRecordConfirmationFinishEvent"
    }

    def ok(self):
        """
        Click <Finish>
        Goes to SCR_0309
        """
        return self.go("finish")