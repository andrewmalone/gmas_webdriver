from pages.Page import Page
from pages.elements import Text


class SCR0190(Page):
	"""
	SCR_0190 Edit indirect cost rates
	"""
	locators = {
		"add": "EditIdcRatesRevisionAddEvent",
		"rate": "css=input[type=text][name$=__rate]",
		"date": "css=input[type=text][name$=__effectiveDate]",
		"ok": "EditIdcRatesRevisionOKEvent"
	}

	rate = Text("rate", "IDC Rate")
	date = Text("date", "Effective Date")

	def add_rate(self):
		"""
		Click <Add rate>
		"""
		return self.go("add")

	def ok(self):
		"""
		Click <Ok>
		Goes to SCR_0474
		"""
		return self.go("ok")