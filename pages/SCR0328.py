from pages.Page import Page
from pages.elements import Text, Select, Radio


class SCR0328(Page):
	locators = {
		"ok" : "name=EditSegmentRevisionAwardInformationDoneEvent",
		"next": "name=EditSegmentRevisionAwardInformationNextEvent",
		"funding instrument": "name=fundingInstrument",
		"payment method": "name=paymentMethodId",
		"loc": "name=agencyLOCNumber",
		"cfda": "name=cfdaNumber",
		"arra": "css=input[name='arraFundingFlag']",
		"ia": "css=input[name='expandedAuthorityFlag']",
		"snap": "css=input[name='snapFlag']",
		"equipment": "css=input[name='specialEquipmentTermsFlag']",
		"agency": "css=input[name='agencyFundFlag']"
	}

	funding_instrument = Select("funding instrument")
	payment_method = Select("payment method")
	loc_number = Text("loc")
	cfda = Text("cfda")
	arra = Radio("arra")
	ia = Radio("ia")
	snap = Radio("snap")
	equipment = Radio("equipment")
	agency = Radio("agency")

	def ok(self):
		return self.go("ok")

	def next(self):
		return self.go("next")
		
