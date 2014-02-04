"""
Base class for Page objects
"""
from selenium.webdriver.support.wait import WebDriverWait
from pages.modules import COM0500, GMAS_Header
from pages.webelement import GMWebElement
import re


class Page(GMWebElement):
    """
    Page object class
    """

    def __init__(self, driver):
        """
        Parameters: webdriver object
        """
        self.env = driver.env
        self.driver = driver
        self.wait = 60
        self.w = WebDriverWait(self.driver, self.wait)
        self.w.until(lambda d: d.find_element_by_css_selector("td.footer"))

        # set up some includes
        #TODO: There must be a better way to do this!
        self.project_snapshot = COM0500(self)
        self.global_header = GMAS_Header(self)

    def get_current_page(self):
        elems = self.find_elements("css=td.footer")
        for elem in elems:
            if "The screen you are on is" in elem.text:
                return re.search('SCR.*', elem.text).group(0)

    def get_page_load_time(self):
        # Doesn't work in PhantomJS yet, fine in Firefox and Chrome
        return self.driver.execute_script("return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart")

    def switch_to_popup(self):
        self.w.until(lambda d: len(d.window_handles) == 2)
        popup_win = self.driver.window_handles[1]
        self.driver.switch_to_window(popup_win)

    def set_fields(self, fields):
        for key, value in fields.iteritems():
            setattr(self, key, value)
        return self

    def load_page(self):
        import importlib
        #TODO: this method assumes we can match based on the footer names. Need to account for any exceptions

        # make sure we aren't on the wait screen
        self.w.until(lambda e: len(e.find_elements_by_css_selector("script[src$='waitScreen.js']")) == 0)
        self.w.until(lambda d: d.find_element_by_css_selector("td.footer"))
        page = re.search("SCR[0-9]{4}[a-z]?", self.get_current_page()).group(0)
        if page == "SCR0104":
            if self.get_current_page() == "SCR0104SegmentHome":
                page = "SCR0104b"
            elif self.get_current_page() == "SCR0104ProjectHome":
                page = "SCR0104a"
        if page == "SCR0089a": page = "SCR0089"
        if page == "SCR0474b": page = "SCR0474"
        cls = getattr(importlib.import_module("pages.%s" % (page)), page)
        return cls(self.driver)

    def refresh(self):
        """
        Reloads the current page object from disk (for debugging)
        """
        import sys
        import importlib
        page = self.__class__.__name__
        module = "pages.%s" % self.__class__.__name__
        reload(sys.modules[module])
        cls = getattr(importlib.import_module("pages.%s" % (page)), page)
        return cls(self.driver)

    def get_id(self, id_name):
        # This will only work if the ID is in a hidden input field
        locator = "css=input[type='hidden'][name='%sId']" % (id_name)
        return self.find_element(locator).get_attribute("value")

    def goto_breadcrumb(self, text):
        crumbs = self.find_elements("css=a.bread")
        for crumb in crumbs:
            if crumb.text == text:
                crumb.click()
                return self.load_page()

    def goto_last_breadcrumb(self):
        crumbs = self.find_elements("css=a.bread")
        crumbs[-1].click()
        return self.load_page()

    def go(self, locator, replace=False):
        self.find(locator, replace).click()
        return self.load_page()

    def goto_segment(self, segment_id):
        url = "https://%s.harvard.edu/gmas/project/SCR0104SegmentHome.jsp?segmentId=%s" % (self.env, segment_id)
        self.driver.get(url)
        return self.load_page()

    def goto_gmashome(self):
        url = "https://%s.harvard.edu/gmas/user/SCR0270GMASHomePage.jsp" % (self.env)
        self.driver.get(url)
        return self.load_page()

    def test_login(self, huid):
        url = "https://%s.harvard.edu/gmas/testLoginServlet?HUID=%s" % (self.env, huid)
        self.driver.get(url)
        return self.load_page()