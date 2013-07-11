from pages.Page import Page
import pages.SCR0105

locators = {
	"ok" : "name=AllocateAwardedFundstoAccountsDoneEvent"
}

class SCR0427(Page):
	def ok(self):
		self.find_element(locators["ok"]).click()
		# wait screen
		self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0105]"))
		return pages.SCR0105.SCR0105(self.driver)

