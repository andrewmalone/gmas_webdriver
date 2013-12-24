from pages.Page import Page

		
class SCR0184(Page):
	"""
	SCR_0184 Create Fund
	"""
	locators = {
		"cancel" : "name=CreateFundCancelEvent",
		"ok": "CreateFundOKEvent"
	}
	
	def cancel(self):
		"""
		Click <Cancel>
		Goes to SCR_0474
		"""
		return self.go("cancel")

	def ok(self):
		"""
		Click <Ok>
		Goes to SCR_0474
		"""
		return self.go("ok")	