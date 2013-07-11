from pages.Page import Page

#TODO add other sponsor lookup
#TODO add methods for lookup by name
#TODO move all popup handling to separate function (possibly into the Page object)

locators = {
	"sponsor lookup" : "css=a[href*='sponsorLookupImage'] img[title='Lookup']",
	"prime sponsor lookup" : "css=a[href*='primeSponsorLookupImage'] img[title='Lookup']",
	"sponsor" : "name=sponsorName",
	"prime sponsor" : "name=primeSponsorName",
	"ok" : "name=EditSponsorInfoDoneEvent",
	"prime pi" : "name=primePiName",
	"prime pi lookup" : "css=a[href*='primePiImage'] img[alt='Lookup']",
	"add other sponsor" : "name=AddOtherSponsorEvent",
	"other sponsor lookup" : "css=a[href*='otherSponsorLookupImage'] img[title='Lookup']",
	"other sponsor role" : "css=input[name*='otherSponsorRole'][value='REPLACE']",
}

class SCR0324(Page):
	def add_other_sponsor_by_type(self,type,role):
		# refactor?
		if len(self.driver.find_elements_by_css_selector("input[name*='otherSponsorName']")) > 0:
			self.remove_other_sponsor()
		else:
			self.find_element(locators["add other sponsor"]).click()
			self.w.until(lambda d: d.find_element_by_css_selector("td.footer"))
		self.find_element(locators["other sponsor lookup"]).click()
		self.w.until(lambda d: len(d.window_handles)==2)
		popup_win = self.driver.window_handles[1]
		self.driver.switch_to_window(popup_win)
		from pages.SCR0536x import SCR0536x
		popup = SCR0536x(self.driver)
		popup.select_type(type)
		popup.search()
		popup.select_first_result()
		popup.ok()
		self.find_element(locators["other sponsor role"].replace("REPLACE",role)).click()
	
	def remove_other_sponsor(self):
		#self.driver.implicitly_wait(0)
		if len(self.driver.find_elements_by_css_selector("input[name*='otherSponsorName']")) > 0:
			self.driver.find_element_by_css_selector("input[name*='otherSponsorName']").clear()
		#self.driver.implicitly_wait(5)
	
	def set_sponsor(self,sponsor=""):
		sponsor_edit = self.find_element(locators["sponsor"])
		sponsor_edit.clear()
		sponsor_edit.send_keys(sponsor)

	def set_prime_sponsor(self,sponsor=""):
		p_sponsor_edit = self.find_element(locators["prime sponsor"])
		p_sponsor_edit.clear()
		p_sponsor_edit.send_keys(sponsor)
		
	def lookup_sponsor(self,sponsor=""):
		self.set_sponsor(sponsor)
		self.find_element(locators["sponsor lookup"]).click()
		# switch to the popup window
		# self.driver.switch_to_window("GMAS_LookupPopup")
		self.w.until(lambda d: len(d.window_handles)==2)
		popup = self.driver.window_handles[1]
		self.driver.switch_to_window(popup)
		from pages.SCR0536x import SCR0536x
		return SCR0536x(self.driver)
		
	def lookup_prime_sponsor(self,sponsor=""):
		self.set_prime_sponsor(sponsor)
		self.find_element(locators["prime sponsor lookup"]).click()
		self.w.until(lambda d: len(d.window_handles)==2)
		popup_win = self.driver.window_handles[1]
		self.driver.switch_to_window(popup_win)
		from pages.SCR0536x import SCR0536x
		return SCR0536x(self.driver)
		
	def lookup_prime_pi_huid(self,huid):
		self.find_element(locators["prime pi"]).clear()
		self.find_element(locators["prime pi"]).send_keys(huid)
		self.find_element(locators["prime pi lookup"]).click()
		self.w.until(lambda d: d.find_element_by_css_selector("img[name='primePiImage'][src*='i_match.gif']"))
		
	def ok(self):
		self.find_element(locators["ok"]).click()
		from pages.SCR0105 import SCR0105
		return SCR0105(self.driver)
		