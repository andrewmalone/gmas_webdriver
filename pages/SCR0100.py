from pages.Page import Page
#import pages.SCR0104b

locators = {
	"check all" : "id=paradigmAll",
	"ok" : "name=EditNotificationOkEvent"
}

class SCR0100(Page):
	def check_all(self):
		self.find_element(locators["check all"]).click()
		
	def ok(self):
		self.find_element(locators["ok"]).click()
		self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0104S]"))
		return self.load_page()
		
#d.find_element_by_id("paradigmAll").click()
#d.find_element_by_name("EditNotificationOkEvent").click()
#w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0104]"))