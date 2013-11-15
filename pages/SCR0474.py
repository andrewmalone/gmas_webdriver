from pages.Page import Page
from pages.elements import Select


class SCR0474(Page):
	"""
	SCR_0474 Add/edit account
	"""
	locators = {
		"account type" : "name=accountType",
		"create fund" : "name=CreateNewFundEvent",
		"cancel" : "name=AddAccountRevisionCancelEvent"
	}

	account_type = Select("account type", "Account type dropdown")
		
	def create_fund(self):
		"""
		Click <Create fund>
		Goes to SCR_0184
		"""
		return self.go("create fund")
		
	def cancel(self):
		"""
		Click <Cancel>
		Goes to SCR_0196
		"""
		return self.go("cancel")	