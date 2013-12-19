from pages.Page import Page
from pages.elements import Select, Text
from pages.lookups import Lookup_root

idc_mapping = {
	"TDC": "Total Direct Costs",
	"MTDC": "Modified Total Direct Costs"
}

class SCR0474(Page):
	"""
	SCR_0474 Add/edit account
	"""
	locators = {
		"account type" : "name=accountType",
		"year": "year",
		"start": "startDate",
		"end": "endDate",
		"idc": "idcBasis",
		"edit rates": "EditIDCRatesForEditAccountRevisionEvent",
		"create fund" : "CreateNewFundEvent",
		"select activity": "activityLookupImage",
		"root text": "rootValue",
		"cancel" : "AddAccountRevisionCancelEvent",
		"ok": "EditAccountWithValidationForRevisionOkEvent"
	}

	account_type = Select("account type", "Account type dropdown")
	year = Text("year", "Year text entry")
	start = Text("start", "Account start date")
	end = Text("end", "Account end date")
	idc_basis = Select("idc", "IDC Basis", idc_mapping)
	root_text = Text("root text")
	root = Lookup_root(root_text, "rootLookupImage")
		
	def create_fund(self):
		"""
		Click <Create fund>
		Goes to SCR_0184
		"""
		return self.go("create fund")

	def edit_rates(self):
		"""
		Click <Edit rates>
		Goes to SCR_0190
		"""
		return self.go("edit rates")

	def select_activity(self):
		"""
		Click <Select> for activity value
		Goes to SCR_0182 (in a popup window)
		"""
		self.find("select activity").click()
		self.switch_to_popup()
		return self.load_page()
		
	def cancel(self):
		"""
		Click <Cancel>
		Goes to SCR_0196
		"""
		return self.go("cancel")

	def ok(self):
		"""
		Click <Ok>
		Goes to SCR_0196
		"""
		return self.go("ok")