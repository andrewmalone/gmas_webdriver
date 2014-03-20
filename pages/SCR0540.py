from pages.Page import Page


class SCR0540(Page):
	"""
	SCR_0540 Standing team org coverage
	"""
	locators = {
		"cancel": "TeamCoverageCancelEvent"
	}

	def cancel(self):
		"""
		Click <Cancel>
		Goes to SCR_0050
		"""
		return self.go("cancel")
