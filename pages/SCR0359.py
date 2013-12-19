from pages.Page import Page
from pages.elements import Text

# ONLY FOR PERIOD ONE SO FAR!!!
class SCR0359(Page):
    locators = {
        "ob_start": "css=[name$='obligatedStartDate']",
        "ob_end": "css=[name$='obligatedEndDate']",
        "next": "name=EditPeriodDatesNextEvent",
        "done": "name=EditPeriodDatesDoneEvent"
    }

    ob_start = Text("ob_start")
    ob_end = Text("ob_end")

    def next(self):
        return self.go("next")

    def done(self):
        return self.go("done")
