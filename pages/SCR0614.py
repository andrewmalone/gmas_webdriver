from pages.Page import Page

locators = {
	
}

class SCR0614(Page):
	locators = locators

	def ok(self):
		self.driver.execute_script("objectSelected()")
		self.driver.switch_to_window(self.driver.window_handles[0])