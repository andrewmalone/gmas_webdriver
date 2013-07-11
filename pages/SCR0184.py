from pages.Page import Page

locators = {
	"cancel" : "name=CreateFundCancelEvent"
}

class fund_type():
	pass
		
class SCR0184(Page):
	def __init__(self,d):
		Page.__init__(self,d)
		
		# set the fund type attributes from the page...
		# Is the fund type editable?
		if self.get_current_page()[:7] == "SCR0184":
			e = self.find_element("name=fundType")
			if e.tag_name == "input":
				default = e.get_attribute("value")[:2]
				editable = False
				options = []
			if e.tag_name == "select":
				editable = True
				opts = e.find_elements_by_css_selector("option")
				options = []
				for o in opts:
					# check for the default
					if o.is_selected():
						if o.text[:2] == "  ":
							default = "none"
						else:
							default = o.text[:2]
					# add to the options
					if o.text[:2] != "  ":
						options.append(o.text[:2])
			
			self.fund_type = fund_type()
			self.fund_type.default = default
			self.fund_type.editable = editable
			self.fund_type.options = options
	
	def nav_to(self,segment_id,revision_id):
		url = "https://%s.harvard.edu/gmas/dispatch?segmentId=%s&segmentRevisionId=%s&formName=AccountRevisionDetailsForm&screenName=%%2Faccount%%2Frevision%%2FSCR0474AddAccountRevision.jsp&accountType=10101&accountStatus=10051&CreateNewFundEvent.x=48&CreateNewFundEvent.y=0&ref=%%2Faccount%%2Frevision%%2FSCR0474AddAccountRevision.jsp&formName=AccountRevisionDetailsForm" %(self.env,segment_id,revision_id)
		self.driver.get(url)
		return SCR0184(self.driver)
	
	def cancel(self):
		self.find_element(locators["cancel"]).click()
		from pages.SCR0474 import SCR0474
		return SCR0474(self.driver)
				
		