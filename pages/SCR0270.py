from pages.Page import Page
from pages.elements import Text

locators = {
    "create proposal": "css=a[href*=HomePageCreateProposalEvent]",
    "recently viewed dropdown": "css=#s option[value='REPLACE']",
    "recently viewed projects": "sizzle=tr:has(a[href*='ProjectListSegmentHomeEvent']):not(tr:has(table))",
    "search": "name=projectSegmentSearchText"
}


class recent_project():
    def __init__(self, row):
        cells = row.find_elements_by_tag_name("td")
        # 1 = project id
        # 5 = link (from title)
        # 9 = PI Name
        # 13 = Sponsor name
        self.project_id = cells[1].text
        self.title = cells[5].text
        self.link = cells[5].find_element_by_tag_name("a")
        self.pi = cells[9].text
        self.sponsor = cells[13].text


class SCR0270(Page):
    """Page object for SCR_0270 GMAS Home

    Attributes:
        search: search box
    """
    locators = locators
    search = Text("search")

    def nav_to(self):
        """Direct navigation to GMAS Home"""
        if self.get_current_page() != "SCR0270GMASHomePage":
            self.driver.get("https:%s.harvard.edu/gmas/user/SCR0270GMASHomePage.jsp" % (self.env))
            return SCR0270(self.driver)
        else:
            return self

    def create_proposal(self):
        """Click on the <Create an initial proposal> button

        Goes to SCR_0088
        """
        self.find("create proposal").click()
        #from pages.SCR0088 import SCR0088
        #return SCR0088(self.driver)
        return self.load_page()

    def set_recently_viewed_projects(self, num):
        self.find_element(locators["recently viewed dropdown"].replace("REPLACE", str(num))).click()
        self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0270]"))
        return SCR0270(self.driver)

    def get_recently_viewed_projects(self):
        rows = self.find_elements(locators["recently viewed projects"])  # a list of tr elements
        tmp = []
        for row in rows:
            if row.is_displayed():
                tmp.append(recent_project(row))
        # self.recently_viewed_projects = tmp
        return tmp
