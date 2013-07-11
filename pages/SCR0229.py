from pages.Page import Page
from pages.elements import Radio


class SCR0229(Page):
    locators = {
        "next": "name=BudgetApprovalsAttributesNextEvent",
        "cost_share": "css=[name='costSharing']",
        "matching": "css=[name='sponsorMatchingFund']",
        "program_income": "css=[name='programIncomeFlag']",
        "on_campus": "css=[name='onOffCampusCode']",
        "admin salary": "css=[name='administrativeSalary']"
    }

    cost_share = Radio("cost_share")
    matching = Radio("matching")
    program_income = Radio("program_income")
    on_campus = Radio("on_campus")
    admin_salary = Radio("admin salary")

    def set_all_radios(self, value):
        radios = self.driver.find_elements_by_css_selector("input[type='radio'][value='%s']" % (value))
        for radio in radios:
            radio.click()

    def ok(self):
        self.find("next").click()
        return self.load_page()
