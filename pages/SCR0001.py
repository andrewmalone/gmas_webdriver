from pages.Page import Page


class SCR0001(Page):
    """
    SCR_0001 Project search
    """
    locators = {
        "result": "css=a[href*='ProjectListSegmentHomeEvent']"
    }

    def goto_first_result(self):
        """
        Clicks the first search result in the list
        Goes to SCR_0104b
        """
        elem = self.finds("result")[0]
        elem.click()
        return self.load_page()