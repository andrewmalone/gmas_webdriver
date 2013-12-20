from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_organization, Lookup_person


class SCR0324(Page):
	"""
	SCR_0324 Edit sponsor information
	"""
	locators = {
		"sponsor" : "name=sponsorName",
		"prime sponsor" : "name=primeSponsorName",
		"ok" : "name=EditSponsorInfoDoneEvent",
		"next": "name=EditSponsorInfoNextEvent",
		"prime pi" : "name=primePiName"
	}

	sponsor_text = Text("sponsor", "Sponsor")
	sponsor = Lookup_organization(sponsor_text, "sponsorLookupImage", "Sponsor")
	prime_sponsor_text = Text("prime sponsor", "Prime sponsor")
	prime_sponsor = Lookup_organization(prime_sponsor_text, "primeSponsorLookupImage", "Prime sponsor")
	prime_pi_text = Text("prime pi", "Prime PI")
	prime_pi = Lookup_person(prime_pi_text, "primePiImage", "Prime PI")
		
	def ok(self):
		"""
		Click <Done making revisions to this section>
		Goes to SCR_0105
		"""
		return self.go("ok")

	def next(self):
		"""
		Click <Next>
		Goes to SCR_0403b
		"""
		return self.go("next")