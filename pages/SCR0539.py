from pages.Page import Page


class SCR0539(Page):
	"""
	SCR_0539 Standing team roles
	"""
	locators = {
		"cancel": "ModifyTeamRoleCancelEvent"
	}

	def cancel(self):
		"""
		Click <Cancel>
		Goes to SCR_0050
		"""
		return self.go("cancel")
