from pages.Page import Page
from pages.elements import Text


class SCR0083(Page):
    locators = {
        "date issued": "name=dateIssued",
        "date received": "name=dateReceivedByHarvard",
        "next": "name=EnterNoticeAttributesNextEvent"
    }

    date_issued = Text("date issued")
    date_received = Text("date received")

    def ok(self):
        self.find("next").click()
        return self.load_page()