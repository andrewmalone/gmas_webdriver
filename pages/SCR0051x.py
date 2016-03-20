from pages.Page import Page


class SCR0051x(Page):
    """
    SCR_0051x Person search (popup)
    """
    locators = {
        "first non-huid": "xpath=(//input[@name='personHUID'][@value='' or @value='null'])[1]/preceding-sibling::input[@type='radio']",
        "ok": "css=img[title='OK']"
    }

    def select_first_non_huid(self):
        """
        Selects the first non-huid person listed in the search result
        """
        self.find("first non-huid").click()

    def ok(self):
        """
        Click <Ok>
        Closes the popup and returns to the main window
        """
        self.find("ok").click()
        # return to the main window
        self.driver.switch_to_window(self.driver.window_handles[0])
