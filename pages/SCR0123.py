
from pages.Page import Page
from pages.elements import Text


class SCR0123(Page):
    """
    SCR_0123 Edit awarded dollars
    """
    locators = {
        "ob_direct": "css=input[type=text][name$=changeObligatedDirect]",
        "ob_indirect": "css=input[type=text][name$=changeObligatedIndirect]",
        "ant_direct": "css=input[type=text][name$=changeAnticipatedDirect]",
        "ant_indirect": "css=input[type=text][name$=changeAnticipatedIndirect]",
        "next": "name=NextOnRecordNoticeTotalsEvent",
        "next_period": "css=[title='Next period']",
        "periods": "xpath=//td[@class='strong'][contains(text(),'Period')]"
    }

    ob_direct = Text("ob_direct", "Obligated direct costs")
    ob_indirect = Text("ob_indirect", "Obligated indirect costs")
    ant_direct = Text("ant_direct", "Anticipated direct costs")
    ant_indirect = Text("ant_indirect", "Anticipated indirect costs")

    @property
    def period_count(self):
        """
        Total number of budget periods
        """
        return self.find("periods").text[12]

    @property
    def current_period(self):
        """
        Current budget period
        """
        return self.find("periods").text[7]

    def next_period(self):
        """
        Click the next period button
        """
        return self.go("next_period")

    def next(self):
        """
        Click <Next>
        Goes to SCR_0549
        """
        return self.go("next")
