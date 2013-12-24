from pages.Page import Page


class SCR0549(Page):
    """
    SCR_0549 Record committed cost share
    """
    locators = {
        "next": "name=RecordCommittedCostShareNextEvent"
    }

    def next(self):
        """
        Click <Next>
        Goes to SCR_0196
        """
        return self.go("next")