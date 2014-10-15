from pages.webelement import GMWebElement
import gmas_webdriver.utilities.xpath as xpath


class COM0500(GMWebElement):
    locators = {
        "segment home": "css=a[href*='ProjectSnapShotSegmentHomeEvent']",
        "dates": xpath.text_sibling("td", "Dates", 2),
        "project_id": xpath.text_sibling("td", "Project ID", 2)
    }

    def __init__(self, page):
        self.page = page
        self.driver = page.driver

    @property
    def start_date(self):
        return self.find("dates").text[:10]

    @property
    def end_date(self):
        return self.find("dates").text[-10:]

    @property
    def project_id(self):
        return self.find("project_id").text

    def _go(self, locator):
        self.find(locator).click()
        return self.page.load_page()

    def goto_segment_home(self):
        return self._go("segment home")


class GMAS_Header(GMWebElement):
    locators = {
        "person link": "css=a[href*='GoMyProfileEvent']",
        "people": "g_people",
        "home": "css=a[href*=GoHomeEvent] img",
        "organizations": "g_organizations"
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

    def goto_home(self):
        return self._go("home")

    def goto_organizations(self):
        return self._go("organizations")

