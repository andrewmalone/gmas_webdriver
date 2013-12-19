from pages.Page import Page
from pages.lookups import Lookup_person
from pages.elements import Text, Checkbox


class SCR0617(Page):
    """
    SCR_0617 Grants.gov submission
    """
    locators = {
        "person name": "name=contactPersonName",
        "agree": "name=disclaimerAgreement",
        "submit": "name=PrepareGrantsGovSubmitEvent"
    }

    name_text = Text("person name", "Person to be contacted text input")
    contact_person = Lookup_person(name_text, "personLookupImage", "Person to be contacted lookup")
    # contact lookup is implemented in a non-standard way, so we need to override
    contact_person.lookup_locator = "css=img[alt='Lookup']"
    agree = Checkbox("agree", "'I agree' checkbox")

    def ok(self):
        """
        Click <Submit to Grants.gov>
        Goes to SCR_0618
        """
        return self.go("submit")