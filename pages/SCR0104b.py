from pages.Page import Page
#import pages.SCR0105

locators = {
    "make revision": 'css=a[href*=SegmentHomeMakeRevisionEvent]',
    "continue revision": "css=a[href*='SegmentHomeEditRevisionEvent']",
    "sponsor notices": "link=Sponsor notices"
}


class SCR0104b(Page):
    locators = locators

    def nav_to(self, segment_id):
        url = "https://%s.harvard.edu/gmas/project/SCR0104SegmentHome.jsp?segmentId=%s" % (self.env, segment_id)
        self.driver.get(url)
        return SCR0104b(self.driver)

    def make_revision(self):
        #self.driver.find_element_by_css_selector(locators["make revision"]).click()
        self.find_element(locators["make revision"]).click()
        self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0105]"))
        from pages.SCR0105 import SCR0105
        return SCR0105(self.driver)

    def continue_revision(self):
        self.find("continue revision").click()
        return self.load_page()

    def goto_notices(self):
        self.find("sponsor notices").click()
        return self.load_page()
