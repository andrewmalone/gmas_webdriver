from pages.webelement import GMWebElement

class COM0500(object):
    def __init__(self, page):
        self.page = page

    def goto_segment_home(self):
        self.page.find_element("css=a[href*='ProjectSnapShotSegmentHomeEvent']").click()
        return self.page.load_page()

class GMAS_Header(GMWebElement):
    locators = {
        "person link": "css=a[href*='GoMyProfileEvent']",
        "people": "g_people"
    }

    def __init__(self, page):
        self.page = page
        self.driver = page.driver

    def _go(self, locator):
        self.find(locator).click()
        return self.page.load_page()

    def goto_person_link(self):
        return self._go("person_link")

    def goto_people(self):
        return self._go("people")