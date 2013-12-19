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
    dir = os.path.dirname(os.path.abspath(__file__))
    cfg = dir + "/config.ini"
    config = ConfigParser.RawConfigParser()
    config.read(cfg)
    HUID = base64.b64decode(config.get("setup", "a"))
    PIN = base64.b64decode(config.get("setup", "b"))
    driver.get("https://%s.harvard.edu/gmas/" % (env))
    w = WebDriverWait(driver, 60)
    w.until(lambda e: e.find_element_by_id("username"))
    driver.find_element_by_id("username").send_keys(HUID)
    driver.find_element_by_id("password").send_keys(PIN)
    driver.find_element_by_css_selector("input.login-button[type=submit][value=Login]").click()


def init(browser, env, splitscreen=False, position="full"):
    # this is so that imports will work (there's probably a better way)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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
    loginGMAS(d, d.env)
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