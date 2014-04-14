from pages.Page import Page
from pages.elements import Radio, Text

type_map = {
    "receipt": "2401",
    "postmark": "2402"
}


class SCR0402b(Page):
    """
    SCR_0402b Edit submission requirements
    """
    locators = {
        "due": "dueToSponsorDate",
        "type": "css=[name=dueDateType]",
        "copies": "numberOfRequiredCopies",
        "ok": "EditSubmissionRequirementsOKEvent"
    }

    due_date = Text("due", "Due to sponsor")
    due_date_type = Radio("type", "Due date type", mapping=type_map)
    copies = Text("copies", "Number of copies")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0115
        """
        return self.go("ok")
