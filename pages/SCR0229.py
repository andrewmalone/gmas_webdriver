from pages.Page import Page
from pages.elements import Radio, Text


class SCR0229(Page):
    """
    SCR_0229 Budget Approvals
    """
    locators = {
        "next": "name=BudgetApprovalsAttributesNextEvent",
        "cost_share": "css=[name='costSharing']",
        "matching": "css=[name='sponsorMatchingFund']",
        "program_income": "css=[name='programIncomeFlag']",
        "on_campus": "css=[name='onOffCampusCode']",
        "admin salary": "css=[name='administrativeSalary']",
        "estimated_cost": "name=totalEstimatedCost"
    }

    cost_share = Radio("cost_share", "Cost share radio button (true/false)")
    matching = Radio("matching", "Matching funds radio button (true/false)")
    program_income = Radio("program_income", "Program income radio button (true/false)")
    on_campus = Radio("on_campus", "On/off campus radio button (true/false)")
    admin_salary = Radio("admin salary", "Admin salaries radio button (true/false)")
    estimated_cost = Text("estimated_cost", "Total estimated cost text box")

    def set_all_radios(self, value):
        """
        Helper method - instead of specifying each radio, you can set them all to true or false
        """
        radios = self.driver.find_elements_by_css_selector("input[type='radio'][value='%s']" % (value))
        for radio in radios:
            radio.click()

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0102
        """
        self.find("next").click()
        return self.load_page()
