from pages.Page import Page

locators = {
	"account type" : "sizzle=select[name='accountType'] option:contains('REPLACE')",
	"create fund" : "name=CreateNewFundEvent",
	"cancel" : "name=AddAccountRevisionCancelEvent"
}

class SCR0474(Page):
	def select_account_type(self,type):
		self.find_element(locators["account type"].replace("REPLACE",type)).click()
		
	def create_fund(self):
		self.find_element(locators["create fund"]).click()
		from pages.SCR0184 import SCR0184
		return SCR0184(self.driver)
		
	def cancel(self):
		self.find_element(locators["cancel"]).click()
		from pages.SCR0196 import SCR0196
		return SCR0196(self.driver)
		