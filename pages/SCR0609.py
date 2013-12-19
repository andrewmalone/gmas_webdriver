from pages.Page import Page


class SCR0609(Page):
    """
    SCR_0609 select Grants.gov forms
    """
    locators = {
        "continue": "name=SubmissionPackageGrantsGovContinueEvent"
    }

    def set_form(self, form_name, value):
        """
        Sets the form to Yes ("true") or No ("false")
        String for form name must match exactly:
        * Research & Related Other Project Info
        * Research & Related Budget
        * PHS398 Modular Budget
        * Planned Enrollment Report
        * PHS 398 Cumulative Inclusion Enrollment Report
        * Research & Related Subaward Budget Attachment(s) Form
        * (etc)
        """
        locator = "css=input[name$=__eFormName][value='%s']" % form_name
        name = self.find_element(locator).get_attribute("name").replace("__eFormName", "__optionalFlag")
        locator = "css=input[name='%s'][value='%s']" % (name, value)
        self.find_element(locator).click()

    def set_all_false(self):
        """
        Sets all optional forms to "No"
        """
        for element in self.find_elements("css=input[type='radio'][value='false']"):
            element.click()

    def ok(self):
        """
        Click <Continue>
        Goes to SCR_0509, SCR_0617, or SCR_0615b
        """
        return self.go("continue")