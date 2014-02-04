from pages.Page import Page
from pages.elements import Radio


class SCR0026(Page):
    """
    SCR_0026 Edit Person
    """
    locators = {
        "user_flag": "css=input[name='isGmasUser']",
        "ok": "EditPersonProfileOkEvent"
    }

    user_flag = Radio("user_flag", "GMAS user flag")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0025
        """
        return self.go("ok")