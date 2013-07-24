from pages.Page import Page
from pages.elements import Radio


class SCR0097(Page):
    """
    SCR_0097 Request Approvals (RGS)
    *Note*: All radio button values are true/false
    """
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

    human_subjects = Radio("human subjects", "Human subjects radio button")
    animals = Radio("animals", "Use of animals radio button")
    biohazards = Radio("biohazards", "Biohazards radio button")
    stem_cells = Radio("stem cells", "Stem cell radio button")
    foreign = Radio("foreign", "Foreign radio button (only for HKS)")
    add_staff = Radio("add staff", "Additional staff/space radio button")
    use_of_name = Radio("use of name", "Use of Harvard name radio button")
    appt_exp = Radio("appointment expiration", "Appointment expiration radio button")

    def set_all_radios(self, value):
        """
        Helper method - sets all radio buttons on the page to true or false
        """
        radios = self.driver.find_elements_by_css_selector("input[type='radio'][value='%s']" % (value))
        for radio in radios:
            radio.click()

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0544, SCR_0612b, or SCR_0322
        """
        self.find("next").click()
        return self.load_page()
