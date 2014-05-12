from pages.Page import Page


class SCR0544(Page):
    """
    SCR_0544 School specific questions
    """
    locators = {
        "next": "name=SchoolSpecificInformationNextEvent",
        "save": "name=SchoolSpecificInformationSaveContinueLaterEvent",
        "cancel": "SchoolSpecificInformationCancelEvent"
    }

    def set_all_radios(self, value):
        """
        Set all radio buttons to true or false
        """
        radios = self.driver.find_elements_by_css_selector("input[type='radio'][value='%s']" % (value))
        for radio in radios:
            radio.click()

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0612b or SCR_0332
        """
        self.find("next").click()
        return self.load_page()

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")

    def save(self):
        """
        Clicks <Save and continue later>
        Goes to SCR_0270 (for initial)
        """
        return self.go("save")
