from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import ConfigParser
import os
import base64


def startBrowser(browser, os="win", download_dir=None):
    if browser == "Firefox":
        return webdriver.Firefox()
    if browser == "Chrome":
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--test-type")
        if download_dir is not None:
            prefs = {"download.default_directory": download_dir}
            chrome_options.add_experimental_option("prefs", prefs)
        return webdriver.Chrome(chrome_options=chrome_options)
    if browser == "IE":
        return webdriver.Ie()
    if browser == "Phantom":
        # not sure why the proxy type needed to be here
        # a = ["--ignore-ssl-errors=yes", "--proxy-type=none"]
        a = ["--ignore-ssl-errors=yes"]
        return webdriver.PhantomJS(service_args=a)
    raise Exception("%s is not a defined browser" % browser)


def init_db(host):
    import cx_Oracle
    from gmas_webdriver.database.hosts import hosts
    host = hosts[host]
    dir = os.path.dirname(os.path.abspath(__file__))
    cfg = dir + "/config.ini"
    config = ConfigParser.RawConfigParser()
    config.read(cfg)
    user = base64.b64decode(config.get("setup", "c"))
    passwd = base64.b64decode(config.get("setup", "d"))
    dbstring = cx_Oracle.makedsn(host["host"], host["port"], host["sid"])
    con = cx_Oracle.connect(user, passwd, dbstring)
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
    driver.find_element_by_id("HarvardKey").click()
    driver.find_element_by_id("username").send_keys(HUID)
    driver.find_element_by_id("password").send_keys(PIN)
    driver.find_element_by_id("submitLogin").click()


def maximize(d):
    """
    Maximize a browser window - since the maximize_window function doesn't
    seem to work in Chrome
    """
    width = d.execute_script("return screen.availWidth")
    height = d.execute_script("return screen.availHeight")
    d.set_window_position(0, 0)
    d.set_window_size(width, height)


def init(browser, env, splitscreen=False, position="full",
         port=None, download_dir=None):
    # this is so that imports will work (there's probably a better way)
    # sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    url = env_url(env)

    d = startBrowser(browser, download_dir=download_dir)
    if splitscreen is True:
        d.set_window_position(1500, 0)
    if position == "full":
        maximize(d)
    if position == "left" or position == "right":
        d.maximize_window()
        # maximize(d)
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
        element.setAttribute('style', original_style +
        "; background: yellow !important; border: 2px solid red !important;");
        setTimeout(function(){
            element.setAttribute('style', original_style);
        }, 500);
    """, element)


def env_url(env):
    instances = {
        "gtrain": "https://gmastraining.harvard.edu",
        "gmasprod": "https://gmas.harvard.edu",
        "gdev": "https://gmasdev.ca.harvard.edu",
        "gtest": "https://gmastest.ca.harvard.edu",
        "gint": "https://gmasint.ca.harvard.edu",
        "gsand": "https://gmassand.ca.harvard.edu"
    }
    try:
        return instances[env]
    except KeyError:
        raise Exception("%s is not a defined GMAS environment" % env)
