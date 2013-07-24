from pages.Page import Page


class SCR0099(Page):
    """
    SCR_0099 Request admin team (RGS)
    """
    locators = {
        "next": "name=GrantsMgmtStaffNextEvent"
    }

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0097
        """
        self.find("next").click()
        return self.load_page()
