from pages.Page import Page


class SCR0544(Page):
    locators = {
        "next": "name=SchoolSpecificInformationNextEvent"
    }

    def set_all_radios(self, value):
        radios = self.driver.find_elements_by_css_selector("input[type='radio'][value='%s']" % (value))
        for radio in radios:
            radio.click()

    def ok(self):
        self.find("next").click()
        return self.load_page()
