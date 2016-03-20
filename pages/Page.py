"""
Base class for Page objects
"""
from selenium.webdriver.support.wait import WebDriverWait
from pages.modules import COM0500, GMAS_Header
from pages.webelement import GMWebElement
from selenium.common.exceptions import NoSuchElementException
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
        self.env_url = driver.env_url
        self.driver = driver
        # self.wait = 60
        self.w = WebDriverWait(self.driver, 60)
        # self.w.until(lambda d: d.find_element_by_css_selector("td.footer") or d.find_element_by_css_selector("footer"))

        # set up some includes
        #TODO: There must be a better way to do this!
        self.project_snapshot = COM0500(self)
        #TODO deprecate this!
        self.global_header = GMAS_Header(self)
        self.header = self.global_header

    @property
    def scr(self):
        # return self.get_current_page()[0:7]
        from pagemap import pagemap
        return pagemap(self.get_current_page())

    @property
    def page_title(self):
        try:
            return self.find_element("css=.title").text
        except:
            return ""

    def get_current_page(self):
        elems = self.find_elements("css=td.footer")
        if len(elems) == 0:
            elems = self.find_elements("css=footer li")
        for elem in elems:
            if "The screen you are on is" in elem.text:
                # this is a hack for now
                if "is: cms" in elem.text:
                    return "cms"
                return re.search('SCR.*', elem.text).group(0)

    def get_page_load_time(self):
        # Doesn't work in PhantomJS yet, fine in Firefox and Chrome
        return self.driver.execute_script("return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart")

    def get_page_load_details(self):
        # total = self.driver.execute_script("return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart")
        server = self.driver.execute_script("return window.performance.timing.responseStart - window.performance.timing.requestStart")
        download = self.driver.execute_script("return window.performance.timing.responseEnd - window.performance.timing.responseStart")
        render = self.driver.execute_script("return window.performance.timing.loadEventEnd - window.performance.timing.responseEnd")
        return "{}|{}|{}".format(server, download, render)

    def switch_to_popup(self):
        self.w.until(lambda d: len(d.window_handles) == 2)
        popup_win = self.driver.window_handles[1]
        self.driver.switch_to_window(popup_win)

    def set_fields(self, fields):
        for key, value in fields.iteritems():
            setattr(self, key, value)
        return self

    def set_mode(self):
        if len(self.find_elements("css=td.footer")) > 0:
            self.mode = "old"
        elif len(self.find_elements("css=footer")) > 0:
            self.mode = "convert"

    def load_page(self):
        import importlib
        #TODO: this method assumes we can match based on the footer names. Need to account for any exceptions

        # make sure we aren't on the wait screen
        self.w.until(lambda e: len(e.find_elements_by_css_selector("script[src$='waitScreen.js']")) == 0)
        # self.w.until(lambda d: d.find_element_by_css_selector("td.footer"))
        # self.w.until(lambda d: d.find_element_by_css_selector("td.footer") or d.find_element_by_css_selector("footer"))
        self.w.until(lambda d: len(d.find_elements_by_css_selector("td.footer")) > 0 or len(d.find_elements_by_css_selector("footer")) > 0)
        page = self.scr
        cls = getattr(importlib.import_module("pages.%s" % (page)), page)
        p = cls(self.driver)
        p.set_mode()
        if p.mode == "convert" and hasattr(p, "_locators"):
            p.locators = p._locators
        return p


    def refresh(self):
        """
        Reloads the current page object from disk (for debugging)
        """
        import sys
        import importlib
        page = self.__class__.__name__
        module = "pages.%s" % self.__class__.__name__
        reload(sys.modules[module])
        reload(sys.modules['pages.elements'])
        cls = getattr(importlib.import_module("pages.%s" % (page)), page)
        return cls(self.driver).load_page()

    def get_id(self, id_name):
        locator = "css=input[type='hidden'][name='%sId']" % (id_name)
        try:
            return self.find_element(locator).get_attribute("value")
        except NoSuchElementException:
            url = self.driver.current_url
            param = "{}Id".format(id_name)
            from utilities.url import url_param
            return url_param(url, param)

    def get_ids(self, id_name):
        # Get a list of Ids from hidden inputs or from urls.

        # start with hidden inputs
        locator = "css=input[type='hidden'][name='%sId']" % (id_name)
        ids = [e.get_attribute("value") for e in self.find_elements(locator)]

        # now do urls
        locator = "css=a[href*=%sId]" % (id_name)
        from utilities.url import url_param
        ids += [url_param(e.get_attribute("href"), "%sId" % id_name) for e in self.find_elements(locator)]

        s = set()
        result = []
        for item in ids:
            if item not in s and item is not None:
                s.add(item)
                result.append(item)

        return result

    def get_breadcrumbs(self):
        if self.mode == "old":
            locator = "css=a.bread"
        elif self.mode == "convert":
            locator = "css=section#breadcrumb a"
        return self.find_elements(locator)

    def goto_breadcrumb(self, text):
        crumbs = self.get_breadcrumbs()
        for crumb in crumbs:
            if crumb.text == text:
                crumb.click()
                return self.load_page()

    def goto_last_breadcrumb(self):
        crumbs = self.get_breadcrumbs()
        crumbs[-1].click()
        return self.load_page()

    def goto_breadcrumb_number(self, number):
        crumbs = self.get_breadcrumbs()
        crumbs[number * -1].click()
        return self.load_page()

    def back(self, number=1):
        return self.goto_breadcrumb_number(number)

    def go(self, locator, replace=False):
        self.find(locator, replace).click()
        return self.load_page()

    def action(self, locator):
        element = self.find(locator)
        if not element.is_displayed():
            self.find_element("css=#actionbar-actions .buttons button").click()
        element.click()
        # deal with a confirmation if it exists?
        dialog = self.find_elements("css=.ui-dialog[style*=block]")
        if len(dialog) == 1:
            # find the active submit button and click it.
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            dialog[0].find_element_by_css_selector("button[type=submit]").click()
            self.w.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog[style*=block]")))
        return self.load_page()

    # TODO: Figure out how to move all goto methods to a common class

    def goto_url(self, url):
        """
        Go to any url and return the related page object
        """
        self.driver.get(url.format(self.env_url))
        return self.load_page()

    def goto_segment(self, segment_id, new=True):
        url = "%s/gmas/project/SCR0104SegmentHome.jsp?segmentId=%s" % (self.env_url, segment_id)
        if new:
            url = "%s/gmas/project/SCR0104SegmentHome.xhtml?segmentId=%s" % (self.env_url, segment_id)
        self.driver.get(url)
        return self.load_page()

    def goto_request(self, segment_id, request_id):
        url = "%s/gmas/request/SCR0115Request.jsp?requestId=%s&segmentId=%s" % (self.env_url, request_id, segment_id)
        self.driver.get(url)
        return self.load_page()

    def goto_gmashome(self):
        url = "%s/gmas/user/SCR0270GMASHomePage.jsp" % (self.env_url)
        self.driver.get(url)
        return self.load_page()

    def goto_person(self, person_id):
        url = "%s/gmas/dispatch?PersonNameLinkEvent=&ref=%%2Fperson%%2FSCR0065PersonSearch.jsp&formName=PersonSearchResultsForm&personId=%s" % (self.env_url, person_id)
        self.driver.get(url)
        return self.load_page()

    def test_login(self, huid):
        url = "%s/gmas/testLoginServlet?HUID=%s" % (self.env_url, huid)
        self.driver.get(url)
        return self.load_page()

    def quit(self):
        self.driver.quit()
