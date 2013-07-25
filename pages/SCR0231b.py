from pages.Page import Page
from pages.elements import Text, Radio, Radio_refresh

locators = {
    "due date": "name=dueToSponsorDate",
    "due date type": "css=[name='dueDateType'][value='REPLACE']",
    "s2s": "css=[name='electronicSubmission'][value='REPLACE']",
    "copies": "name=numberOfRequiredCopies",
    "mailing": "name=mailingInstructions",
    "next": "name=EnterSubmissionDetailsNextEvent"
}


class SCR0231b(Page):
    """
    SCR_0231b Submission details for s2s
    """
    locators = locators
    due_date = Text("due date", "Due date text input")
    due_date_type = Radio("due date type", "Due date type radio button\n\
        * 2401 = Receipt date\n\
        * 2402 = Postmark date")  # vals = 2401/2402
    s2s = Radio_refresh("s2s", "S2S radio button (true/false)")
    copies = Text("copies", "text box for number of copied")
    mailing = Text("mailing", "Mailing instructions")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0090
        """
        self.find("next").click()
        from pages.SCR0090 import SCR0090
        return SCR0090(self.driver)

