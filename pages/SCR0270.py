from pages.Page import Page
from pages.elements import Text, Select

locators = {
    "create proposal": "css=a[href*=HomePageCreateProposalEvent]",
    "recent project dropdown": "id=s",
    "recently viewed projects": "xpath=//tr[td[a[contains(@href,'ProjectListSegmentHomeEvent')]]]",
    "search box": "name=projectSegmentSearchText",
    "search": "name=ProjectSearchEvent"
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
    """
    SCR_0270 GMAS Home
    """
    locators = locators
    search_text = Text("search box", "Fund/project search box")
    recent_project_dropdown = Select("recent project dropdown", "Dropdown for recently viewed project")

    def nav_to(self):
        """
        Direct navigation to GMAS Home
        """
        if self.get_current_page() != "SCR0270GMASHomePage":
            self.driver.get("https:%s.harvard.edu/gmas/user/SCR0270GMASHomePage.jsp" % (self.env))
            return SCR0270(self.driver)
        else:
            return self

    def create_proposal(self):
        """
        Click on the <Create an initial proposal> button, Goes to SCR_0088
        """
        self.find("create proposal").click()
        return self.load_page()

    def get_recent_projects_list(self):
        """
        Returns a list of recently viewed projects. Each item in the list contains the following elements:
        * project_id
        * title
        * link (the a element - can be clicked through webdriver)
        * pi
        * sponsor
        """
        rows = self.find_elements(locators["recently viewed projects"])  # a list of tr elements
        tmp = []
        for row in rows:
            if row.is_displayed():
                tmp.append(recent_project(row))
        return tmp

    def search(self):
        """
        Click the <Search> button
        Goes to SCR_0001 or SCR_0104b
        """
        return self.go("search")
