from pages.Page import Page
from pages.elements import Text, Radio

locators = {
    "due date": "name=dueToSponsorDate",
    "due date type": "css=[name='dueDateType'][value='REPLACE']",
    "copies": "name=numberOfRequiredCopies",
    "next": "name=RequestSubmissionDetailsNextEvent"
}


class SCR0231(Page):
    locators = locators
    due_date = Text("due date")
    due_date_type = Radio("due date type")  # vals = 2401/2402
    copies = Text("copies")

    def ok(self):
        self.find("next").click()
        from pages.SCR0090 import SCR0090
        return SCR0090(self.driver)

