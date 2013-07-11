from pages.Page import Page


class SCR0650(Page):
    locators = {
        "links": "css=a[href*='ProjectListSegmentHomeEvent']"
    }

    def nav_to(self, person_id):
        url = "https://%s.harvard.edu/gmas/dispatch?ref=%%2Fperson%%2FSCR0025PersonProfile.jsp&formName=PersonProfileForm&personId=%s&ViewResearchTeamsEvent=" % (self.env, person_id)
        self.driver.get(url)
        return self

    def count_links(self):
        return len(self.finds("links"))

    def count_active_links(self):
        tables = self.find_elements("css=span.defred ~ table")
        if len(tables) == 0:
            return 0
        for table in tables:
            if table.find_element_by_css_selector("td.strong").text == "Active Projects":
                return len(table.find_elements_by_css_selector("a[href*='ProjectListSegmentHomeEvent']"))
        return 0

    def count_pending_links(self):
        tables = self.find_elements("css=span.defred ~ table")
        if len(tables) == 0:
            return 0
        for table in tables:
            if table.find_element_by_css_selector("td.strong").text == "Pending Projects":
                return len(table.find_elements_by_css_selector("a[href*='ProjectListSegmentHomeEvent']"))
        return 0

    def get_url(self, person_id):
        url = "https://%s.harvard.edu/gmas/dispatch?ref=%%2Fperson%%2FSCR0025PersonProfile.jsp&formName=PersonProfileForm&personId=%s&ViewResearchTeamsEvent=" % (self.env, person_id)
        return url
