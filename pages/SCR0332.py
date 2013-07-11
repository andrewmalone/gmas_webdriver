from pages.Page import Page


class SCR0332(Page):
    locators = {
        "go request": "name=FinishGoToRequestEvent"
    }

    def go_req(self):
        self.find("go request").click()
        self.w.until(lambda e: len(e.find_elements_by_css_selector("script[src$='waitScreen.js']")) == 0)
        self.w.until(lambda d: d.find_element_by_css_selector("td.footer"))
        return self.load_page()
        # goes to wait screen! need to add this