from pages.Page import Page
from pages.elements import Text

# ONLY FOR PERIOD ONE SO FAR!!!
class SCR0359(Page):
    """
    SCR_0359 Edit dates in revision
    **NOTE:** currently only supports editing the first period
    """
    locators = {
        "ob_start": "css=[name$='obligatedStartDate']",
        "ob_end": "css=[name$='obligatedEndDate']",
        "next": "name=EditPeriodDatesNextEvent",
        "done": "name=EditPeriodDatesDoneEvent"
    }

    ob_start = Text("ob_start", "Obligated start date")
    ob_end = Text("ob_end", "Obligated end date")

    def next(self):
        """
        Click <Next>
        Goes to SCR_0123
        """
        return self.go("next")

    def done(self):
        """
        Click <Done making revisions to this section
        Goes to SCR_0105
        """
        return self.go("done")
