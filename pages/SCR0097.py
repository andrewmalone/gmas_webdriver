from pages.Page import Page
from pages.elements import Radio


class SCR0097(Page):
    locators = {
        "next": "name=ApprovalQuestionsNextEvent",
        "human subjects": "css=input[value='1707'] + tr input[type='radio']",
        "animals": "css=input[value='1703'] + tr input[type='radio']",
        "biohazards": "css=input[value='1704'] + tr input[type='radio']",
        "stem cells": "css=input[value='1711'] + tr input[type='radio']",
        "foreign": "css=input[value='1706'] + tr input[type='radio']",
        "add staff": "css=input[value='1701'] + tr input[type='radio']",
        "use of name": "css=input[value='1710'] + tr input[type='radio']",
        "appointment expiration": "css=input[value='1709'] + tr input[type='radio']"
    }

    human_subjects = Radio("human subjects")
    animals = Radio("animals")
    biohazards = Radio("biohazards")
    stem_cells = Radio("stem cells")
    foreign = Radio("foreign")
    add_staff = Radio("add staff")
    use_of_name = Radio("use of name")
    appt_exp = Radio("appointment expiration")

    def set_all_radios(self, value):
        radios = self.driver.find_elements_by_css_selector("input[type='radio'][value='%s']" % (value))
        for radio in radios:
            radio.click()

    def ok(self):
        self.find("next").click()
        return self.load_page()
