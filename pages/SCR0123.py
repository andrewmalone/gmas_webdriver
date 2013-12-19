from pages.Page import Page
from pages.elements import Text


class SCR0123(Page):
    locators = {
        "ob_direct": "css=input[type=text][name$=changeObligatedDirect]",
        "ob_indirect": "css=input[type=text][name$=changeObligatedIndirect]",
        "ant_direct": "css=input[type=text][name$=changeAnticipatedDirect]",
        "ant_indirect": "css=input[type=text][name$=changeAnticipatedIndirect]",
        "next": "name=NextOnRecordNoticeTotalsEvent",
        "next_period": "css=[title='Next period']"
    }

    ob_direct = Text("ob_direct")
    ob_indirect = Text("ob_indirect")
    ant_direct = Text("ant_direct")
    ant_indirect = Text("ant_indirect")

    def next_period(self):
        return self.go("next_period")

    def next(self):
        return self.go("next")