from pages.Page import Page
from pages.elements import Text, Row, Radio


class SCR0006(Page):
    """
    SCR_0006 Edit initial/competing budget
    """
    locators = {
        "total_direct": "name=totalDirectCost",
        "total_indirect": "name=totalIndirectCost",
        "edit indirect": "name=EditProposedBudgetEditIndirectCostEvent",
        "editbox": "css=input[name$='__budgetEntryAmount']",
        "next period": "css=input[title='Next period']",
        "ok": "name=EditProposedBudgetOKEvent",
        "cancel": "EditProposedBudgetCancelEvent",
        "subagreement_row": "xpath=//a[contains(@onclick,'setSubagreementIdAndSubmitForm')]/ancestor::tr[1]",
        "periods": "xpath=//td[@class='strong'][contains(text(),'Period')]",
        "level": "css=input[name=recordByBudgetLevel]",
        "category_row": "xpath=//input[@type='text'][contains(@name,'segmentCategoryBudgetEntryAmount')]/ancestor::tr[1]",
        "person_salary_row": "xpath=//a[contains(@href,'setSCR252fields')]/ancestor::tr[1]"
    }

    total_direct = Text("total_direct", "Total direct cost")
    total_indirect = Text("total_indirect", "Total indirect cost")
    budget_level = Radio("level", "Budget level", mapping={
        "total": "9776",
        "category": "9777",
        "line item": "9778"
        })

    def enter_first(self, amount):
        """
        Enters a budget amount in the first available edit box
        (only works with category/line item budgets)
        """
        elems = self.finds("editbox")
        for elem in elems:
            if elem.is_displayed() is True:
                elem.send_keys(amount)
                break

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

    def next(self):
        """
        Click the next period arrow
        """
        return self.go("next period")

    def edit_indirect(self):
        """
        Click <Edit indirect costs>
        Goes to SCR_0018
        """
        return self.go("edit indirect")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0031 or SCR_0115
        """
        return self.go("ok")

    def cancel(self):
        """
        Click <Cancel>
        Goes to SCR_0115
        """
        return self.go("cancel")

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
            "link": "css=a"
        }

        def go(self):
            """
            Click the subagreement link
            Goes to SCR_00017
            """
            return self._go("link")

    @property
    def category_count(self):
        """
        Number of categories
        """
        return len(self.finds("category_row"))

    def category(self, n):
        """
        Returns the nth category row
        //Category
        """
        row = self.finds("category_row")[n - 1]
        return self.Category(row, self)

    class Category(Row):
        locators = {
            "input": "css=input[type=text]"
        }

        amount = Text("input", "Category amount entry")

    @property
    def person_count(self):
        """
        Count of people
        """
        # dividing by two here because each person appears twice for salary and fringe
        return len(self.finds("person_salary_row")) / 2

    def person(self, n):
        """
        Returns the nth person
        //Person_salary
        """
        row = self.finds("person_salary_row")[n - 1]
        return self.Person_salary(row, self)

    class Person_salary(Row):
        locators = {
            "link": "css=a"
        }

        def go(self):
            """
            Click the person link
            Goes to SCR_0252
            """
            return self._go("link")
