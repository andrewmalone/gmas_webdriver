from pages.Page import Page
from pages.elements import Text, Radio, Radio_refresh

locators = {
    "due date": "name=dueToSponsorDate",
    "due date type": "css=[name='dueDateType'][value='REPLACE']",
    "s2s": "css=[name='electronicSubmission'][value='REPLACE']",
    "copies": "name=numberOfRequiredCopies",
    "next": "name=EnterSubmissionDetailsNextEvent"
}


class SCR0231b(Page):
    locators = locators
    due_date = Text("due date")
    due_date_type = Radio("due date type")  # vals = 2401/2402
    s2s = Radio_refresh("s2s")
    copies = Text("copies")

    def ok(self):
        self.find("next").click()
        from pages.SCR0090 import SCR0090
        return SCR0090(self.driver)

