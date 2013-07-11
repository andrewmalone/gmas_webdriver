from pages.Page import Page

locators = {
	"ok" : "name=EditSegmentRevisionAwardInformationDoneEvent",
	"funding instrument" : "sizzle=select[name='fundingInstrument'] option:contains('REPLACE')"
}

class SCR0328(Page):		
	def ok(self):
		self.find_element(locators["ok"]).click()
		# wait screen is here!
		self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0105]"))
		from pages.SCR0105 import SCR0105
		return SCR0105(self.driver)
		
	def set_funding_instrument(self,fi):
		self.find_element(locators["funding instrument"].replace("REPLACE",fi)).click()
