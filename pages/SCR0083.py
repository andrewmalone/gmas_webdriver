from pages.Page import Page
from pages.elements import Text


class SCR0083(Page):
    """
    SCR_0083 Enter notice attributes
    """
    locators = {
        "date issued": "name=dateIssued",
        "date received": "name=dateReceivedByHarvard",
        "award number": "name=sponsorAwardNumber",
        "next": "name=EnterNoticeAttributesNextEvent"
    }

    date_issued = Text("date issued", "Date issued")
    date_received = Text("date received", "Date received")
    award_number = Text("award number", "Award number")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0377
        """
        return self.go("next")