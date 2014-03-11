from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import ConfigParser
import os
import sys
import base64


def startBrowser(browser, os="win"):
    if browser == "Firefox":
        return webdriver.Firefox()
    if browser == "Chrome":
        return webdriver.Chrome()
    if browser == "IE":
        return webdriver.Ie()
    if browser == "Phantom":
        return webdriver.PhantomJS()
        a = ["--ignore-ssl-errors=yes", "--proxy-type=none"]
        str = ""
        if os == "win":
            str = ".exe"
            return webdriver.PhantomJS(executable_path="/phantomjs%s" % (str), service_args=a)
        else:
            return webdriver.PhantomJS(service_args=a)
        #return webdriver.PhantomJS(executable_path="/phantomjs%s" %(str))
    raise Exception("%s is not a defined browser" % browser)

def init_db(database):
    import cx_Oracle
    dir = os.path.dirname(os.path.abspath(__file__))
    cfg = dir + "/config.ini"
    config = ConfigParser.RawConfigParser()
    config.read(cfg)
    user = base64.b64decode(config.get("setup", "c"))
    passwd = base64.b64decode(config.get("setup", "d"))
    con = cx_Oracle.connect("%s/%s@%s" % (user, passwd, database))
    return con.cursor()

def loginGMAS(driver):
    dir = os.path.dirname(os.path.abspath(__file__))
    cfg = dir + "/config.ini"
    config = ConfigParser.RawConfigParser()
    config.read(cfg)
    HUID = base64.b64decode(config.get("setup", "a"))
    PIN = base64.b64decode(config.get("setup", "b"))
    driver.get("%s/gmas" % driver.env_url)
    w = WebDriverWait(driver, 60)
    w.until(lambda e: e.find_element_by_id("username"))
    driver.find_element_by_id("username").send_keys(HUID)
    driver.find_element_by_id("password").send_keys(PIN)
    driver.find_element_by_css_selector("input.login-button[type=submit][value=Login]").click()


def init(browser, env, splitscreen=False, position="full", port=None):
    # this is so that imports will work (there's probably a better way)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    url = env_url(env)

    d = startBrowser(browser)
    if splitscreen is True:
        d.set_window_position(1500,0)
    if position == "full":
        d.maximize_window()
    if position == "left" or position == "right":
        d.maximize_window()
        size = d.get_window_size()
        pos = d.get_window_position()
        d.set_window_size(size["width"]/2, size["height"])
        x = pos["x"] if position == "left" else pos["x"] + size["width"]/2
        d.set_window_position(x, pos["y"])
    d.env = env
    d.env_url = url
    loginGMAS(d)
    from pages.SCR0270 import SCR0270
    p = SCR0270(d).nav_to()
    return p


def highlight(element):
    """Highlights (blinks) a Webdriver element.
    In pure javascript, as suggested by https://github.com/alp82.
    """
    driver = element.parent
    driver.execute_script("""
        element = arguments[0];
        original_style = element.getAttribute('style');
        element.setAttribute('style', original_style + "; background: yellow; border: 2px solid red;");
        setTimeout(function(){
            element.setAttribute('style', original_style);
        }, 500);
    """, element)

def env_url(env):
    instances = {
        "gdev": "https://gmasdev.cadm.harvard.edu",
        "gtest": "https://gmastest.cadm.harvard.edu",
        "gtrain": "https://gmastraining.harvard.edu",
        "gprod": "https://gmas.harvard.edu",
        "gdev_new": "https://gmasdev.ca.harvard.edu"
    }
    try:
        return instances[env]
    except KeyError:
        raise Exception("%s is not a defined GMAS environment" % env)