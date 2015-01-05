from pages.Page import Page


class SCR0511(Page):
    """
    SCR_0511 subactivity detail
    """
    locators = {
        "disable": "DisableSubactivityEvent"
    }

    def disable(self):
        """
        Click the <Disable subactivity> button
        Goes to SCR_0602a or stays on the current page with an error
        """
        return self.go("disable")
