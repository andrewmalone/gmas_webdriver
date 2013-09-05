class COM0500(object):
    def __init__(self, page):
        self.page = page

    def goto_segment_home(self):
        self.page.find_element("css=a[href*='ProjectSnapShotSegmentHomeEvent']").click()
        return self.page.load_page()

class GMAS_Header(object):
    def __init__(self, page):
        self.page = page

    def goto_person_link(self):
        self.page.find_element("css=a[href*='GoMyProfileEvent']").click()
        return self.page.load_page()