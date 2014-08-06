from pages.Page import Page
from pages.elements import Text, Select, Row


class SCR0270(Page):
    """
    SCR_0270 GMAS Home
    """
    locators = {
        "create proposal": "css=a[href*=HomePageCreateProposalEvent]",
        "recent project dropdown": "id=s",
        "recently viewed projects": "xpath=//tr[td[a[contains(@href,'ProjectListSegmentHomeEvent')]]]",
        "search box": "name=projectSegmentSearchText",
        "search": "name=ProjectSearchEvent",
        "loc": "link=Letter of Credit",
        "documents": "name=g_documentsoff",
        "organizations": "name=g_organizations",
        "standing teams": "event=ViewStandingTeamEvent",
        "security": "event=ViewSecurityDetailsEvent"
    }

    search_text = Text("search box", "Fund/project search box")
    recent_project_dropdown = Select("recent project dropdown", "Dropdown for recently viewed project")

    def nav_to(self):
        """
        Direct navigation to GMAS Home
        """
        if self.get_current_page() != "SCR0270GMASHomePage":
            self.driver.get("%s/gmas/user/SCR0270GMASHomePage.jsp" % (self.env_url))
            return SCR0270(self.driver)
        else:
            return self

    def create_proposal(self):
        """
        Click on the <Create an initial proposal> button, Goes to SCR_0088
        """
        return self.go("create proposal")

    def recent_project(self, n):
        """
        Returns the nth row from the recent projects list
        //Recent_project
        """
        row = self.finds("recently viewed projects")[n - 1]
        return self.Recent_project(row, self)

    def search(self):
        """
        Click the <Search> button
        Goes to SCR_0001 or SCR_0104b
        """
        return self.go("search")

    def goto_loc(self):
        """
        Clicks the "Letter of Credit" link
        Goes to SCR_0630
        """
        return self.go("loc")

    def goto_doc_clipboard(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0139
        """
        return self.go("documents")

    def goto_organizations(self):
        """
        Clicks the "organizations" link
        Goes to SCR_0067
        """
        return self.go("organizations")

    def goto_standing_teams(self):
        """
        Clicks the "Standing Teams" link
        Goes to SCR_0066
        """
        return self.go("standing teams")

    def goto_security(self):
        """
        Clicks the "Security" link
        Goes to SCR_0287
        """
        return self.go("security")

    class Recent_project(Row):
        # def __init__(self, row):
        #     cells = row.find_elements_by_tag_name("td")
        #     # 1 = project id
        #     # 5 = link (from title)
        #     # 9 = PI Name
        #     # 13 = Sponsor name
        #     self.project_id = cells[1].text
        #     self.title = cells[5].text
        #     self.link = cells[5].find_element_by_tag_name("a")
        #     self.pi = cells[9].text
        #     self.sponsor = cells[13].text
        locators = {
            "link": "css=a"
        }

        def go(self):
            """
            Clicks a recent project link
            Goes to SCR_0104b
            """
            return self._go("link")
