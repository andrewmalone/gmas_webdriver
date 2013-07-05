from selenium import webdriver
import ConfigParser


def startBrowser(browser, os="win"):
    if browser == "Firefox":
        return webdriver.Firefox()
    if browser == "Chrome":
        return webdriver.Chrome()
    if browser == "Phantom":
        a = ["--ignore-ssl-errors=yes", "--proxy-type=none"]
        str = ""
        if os == "win":
            str = ".exe"
            return webdriver.PhantomJS(executable_path="/phantomjs%s" % (str), service_args=a)
        else:
            return webdriver.PhantomJS(service_args=a)
        #return webdriver.PhantomJS(executable_path="/phantomjs%s" %(str))


def loginGMAS(driver, env):
    config = ConfigParser.RawConfigParser()
    config.read("config.ini")
    HUID = config.get("Credentials", "HUID")
    PIN = config.get("Credentials", "PIN")
    driver.get("https://%s.harvard.edu/gmas/" % (env))
    driver.find_element_by_id("authenId").send_keys(HUID)
    driver.find_element_by_id("authenPassword").send_keys(PIN)
    driver.find_element_by_css_selector("input.login-button[type=submit][value=Login]").click()


def init(browser, env):
    d = startBrowser(browser)
    d.env = env
    loginGMAS(d, d.env)
    from pages.SCR0270 import SCR0270
    p = SCR0270(d).nav_to()
    return p
