from pages.Page import Page
from pages.elements import Text, Radio

locators = {
    "due date": "name=dueToSponsorDate",
    "due date type": "css=[name='dueDateType'][value='REPLACE']",
    "copies": "name=numberOfRequiredCopies",
    "mailing": "name=mailingInstructions",
    "next": "name=RequestSubmissionDetailsNextEvent",
    "cancel": "RequestSubmissionDetailsCancelEvent"
}


class SCR0231(Page):
    """
    SCR_0231 Submission Details
    """
    locators = locators
    due_date = Text("due date", "Due date text input")
    due_date_type = Radio("due date type", "Due date type radio button\n\
        * 2401 = Receipt date\n\
        * 2402 = Postmark date")  # vals = 2401/2402
    copies = Text("copies", "Number of copies text input")
    mailing = Text("mailing", "Mailing instructions")

    def ok(self):
        """
        Click the <Next> button.
        Goes to SCR_0090, SCR_0461 (SNAP for continuations)
        """
        self.find("next").click()
        return self.load_page()

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")
