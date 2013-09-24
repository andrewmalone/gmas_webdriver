from pages.Page import Page
from pages.elements import Text, Select, Radio


class SCR0328(Page):
	locators = {
		"ok" : "name=EditSegmentRevisionAwardInformationDoneEvent",
		"funding instrument" : "name=fundingInstrument",
		"payment method": "name=paymentMethodId",
		"loc": "name=agencyLOCNumber",
		"cfda": "name=cfdaNumber",
		"arra": "css=input[name='arraFundingFlag']"
	}

	funding_instrument = Select("funding instrument")
	payment_method = Select("payment method")
	loc_number = Text("loc")
	cfda = Text("cfda")
	arra = Radio("arra")


	def ok(self):
		return self.go("ok")
		
