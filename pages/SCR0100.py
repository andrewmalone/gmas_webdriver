from pages.Page import Page
from pages.elements import Checkbox


class SCR0100(Page):
	"""
	SCR_0100 Select notification recipients
	"""
	locators = {
		"check all" : "id=paradigmAll",
		"ok" : "name=EditNotificationOkEvent"
	}

	check_all = Checkbox("check all", "Check/uncheck all recipients")
		
	def ok(self):
		"""
		Click <Ok>
		Goes to SCR_0104b (if commiting revision)
		"""
		# TODO - there are more destinations to document for this screen!
		return self.go("ok")