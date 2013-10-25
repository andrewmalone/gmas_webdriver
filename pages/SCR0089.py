from pages.Page import Page
from pages.elements import Text, Select, Radio
# from pages.lookups import Lookup_person, Lookup_organization

locators = {
    "title": "name=requestTitle",
    "sponsor": "name=sponsor",
    "sponsor lookup": "css=a[href*='sponsorValidatedImage'] img",
    "sponsor lookup match": "css=img[name='sponsorValidatedImage'][src$='i_match.gif']",
    "prime sponsor": "name=primeSponsor",
    "prime sponsor lookup": "css=a[href*='primeSponsorValidatedImage'] img",
    "pi": "name=piName",
    "pi lookup": "css=a[href*='piImage'] img",
    "pi lookup match": "css=img[name='piImage'][src$='i_match.gif']",
    "mentor": "name=mentorInvestigatorName",
    "mentor lookup": "css=a[href*='mentorValidatedImage'] img",
    "mentor lookup match": "css=img[name='mentorValidatedImage'][src$='i_match.gif']",
    "prime pi": "name=primePiName",
    "prime pi lookup": "css=a[href*='primePiImage'] img",
    "prime pi lookup match": "css=img[name='primePiImage'][src$='i_match.gif']",
    "A21": "name=a21functionalId",
    "discipline": "name=disciplineId",
    "rfp": "css=input[name='isInResponseToRFP'][value='REPLACE']",
    "subs": "css=input[name='hasSubAgreements'][value='REPLACE']",
    "ifi": "css=input[name='isOtherSchoolSharing'][value='REPLACE']",
    "comment": None,
    "cancel": None,
    "back": None,
    "next": "name=CreateInitialRequestNextEvent"
}


class Lookup_pi(object):
    """
    Performs the PI lookup - needs an HUID
    """
    def __set__(self, obj, val):
        obj._lookup_pi(val)

    def __get__(self, obj, type=None):
        pass


class Lookup_mentor(object):
    """
    Performs the Mentor lookup - needs an HUID
    """
    def __set__(self, obj, val):
        obj._lookup_mentor(val)

    def __get__(self, obj, type=None):
        pass

class Lookup_sponsor(object):
    """
    Performs a search for sponsor - will select the first result from the popup window
    """
    def __set__(self, obj, val):
        obj._lookup_sponsor(val)

    def __get__(self, obj, type=None):
        pass


class Lookup_prime_sponsor(object):
    """
    Performs a search for prime sponsor - will select the first result from the popup window
    """
    def __set__(self, obj, val):
        obj._lookup_prime_sponsor(val)

    def __get__(self, obj, type=None):
        pass


class Lookup_prime_pi(object):
    """
    Performs a search for prime PI (needs HUID)
    """
    def __set__(self, obj, val):
        obj._lookup_prime_pi(val)

    def __get__(self, obj, type=None):
        pass


class SCR0089(Page):
    """
    SCR_0089
    """
    locators = locators
    title = Text("title", "Project title")
    sponsor_text = Text("sponsor", "Sponsor name text input")
    sponsor = Lookup_sponsor()
    prime_sponsor_text = Text("prime sponsor", "Prime sponsor name text input")
    prime_sponsor = Lookup_prime_sponsor()
    pi_text = Text("pi", "PI name text input box")
    pi = Lookup_pi()
    mentor_text = Text("mentor", "Mentor name text input box")
    mentor = Lookup_mentor()
    prime_pi_text = Text("prime pi", "Prime PI name text input box")
    prime_pi = Lookup_prime_pi()
    a21 = Select("A21", "A21 dropdown")
    discipline = Select("discipline", "Discipline dropdown")
    rfp = Radio("rfp", "RFP question radio button (true/false)")
    subs = Radio("subs", "Subagreement question radio button (true/false)")
    ifi = Radio("ifi", "IFI radio button question (true/false)")

    def _lookup_sponsor(self, sponsor):
        self.sponsor_text = sponsor
        self.find("sponsor lookup").click()
        self.switch_to_popup()
        from pages.SCR0536x import SCR0536x
        popup = SCR0536x(self.driver)
        popup.select_first_result()
        popup.ok()
        return self

    def _lookup_prime_sponsor(self, sponsor):
        self.prime_sponsor_text = sponsor
        self.find("prime sponsor lookup").click()
        self.switch_to_popup()
        from pages.SCR0536x import SCR0536x
        popup = SCR0536x(self.driver)
        popup.select_first_result()
        popup.ok()
        return self

    def _lookup_pi(self, pi):
        self.pi_text = pi
        self.find("pi lookup").click()
        self.w.until(lambda e: self.find("pi lookup match"))
        return self

    def _lookup_mentor(self, mentor):
        self.mentor_text = mentor
        self.find("mentor lookup").click()
        self.w.until(lambda e: self.find("mentor lookup match"))
        return self

    def _lookup_prime_pi(self, pi):
        self.prime_pi_text = pi
        self.find("prime pi lookup").click()
        self.w.until(lambda e: self.find("prime pi lookup match"))
        return self

    def ok(self):
        """
        Clicks the <Ok> button
        Goes to SCR_0613 or SCR_0231
        """
        self.find("next").click()
        return self.load_page()
