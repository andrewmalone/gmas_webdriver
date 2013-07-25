from pages.Page import Page


class SCR0332(Page):
    """
    SCR_0332 Finish request guided steps
    """
    locators = {
        "go request": "name=FinishGoToRequestEvent"
    }

    def go_req(self):
        """
        Click <Finish and go to request>
        Goes to SCR_0115 (through the wait screen)
        """
        self.find("go request").click()
        self.w.until(lambda e: len(e.find_elements_by_css_selector("script[src$='waitScreen.js']")) == 0)
        self.w.until(lambda d: d.find_element_by_css_selector("td.footer"))
        return self.load_page()