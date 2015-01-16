from gmas_webdriver.setup import init

p = init("Firefox", "gdev")
print p.get_current_page()
