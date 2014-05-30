from pages.Page import Page
from pages.elements import Row
import utilities.xpath as xpath


class SCR0031(Page):
    """
    SCR_0031 View proposal budget
    """
    locators = {
        "edit": "ViewProposedBudgetEditPostsubmissionEvent",
        "indirect": "event=ViewProposedBudgetViewIndirectCostRateEvent",
        "modular": "event=ViewProposedBudgetViewModularBudgetEvent",
        "next period": "css=input[title='Next period']",
        "periods": "xpath=//td[@class='strong'][contains(text(),'Period')]",
        "subagreement_row": xpath.parent_row_of_event("ViewProposedBudgetSubagreementEvent")
    }

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

    def edit(self):
        """
        Click the <Edit proposal budget> button
        Goes to SCR_0006 (for initial/competing)
        """
        return self.go("edit")

    def goto_indirect(self):
        """
        Click "Total indirect costs"
        Goes to SCR_0410
        """
        return self.go("indirect")

    def goto_modular(self):
        """
        Click "View modular budget"
        Goes to SCR_0438
        """
        return self.go("modular")

    def has_modular(self):
        """
        Returns True/False depending on if there is a modular budget link
        """
        if len(self.finds("modular")) == 0:
            return False
        else:
            return True

    def next(self):
        """
        Click the next period button
        """
        return self.go("next period")

    @property
    def subagreement_count(self):
        """
        Number of subagreements in the budget
        """
        return len(self.finds("subagreement_row"))

    def subagreement(self, n):
        """
        Returns the nth subagreement row in the budget
        //Subagreement
        """
        element = self.finds("subagreement_row")[n - 1]
        return self.Subagreement(element, self)

    class Subagreement(Row):
        locators = {
            "link": "event=ViewProposedBudgetSubagreementEvent"
        }

        def go(self):
            """
            Click the subagreement link
            Goes to SCR_00017
            """
            return self._go("link")
