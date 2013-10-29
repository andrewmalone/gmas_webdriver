from pages.Page import Page
from pages.elements import Text, Select
from pages.lookups import Lookup_person


class SCR0401(Page):
    """
    SCR_0401 Request submission
    """
    locators = {
        "date received": "name=dateReceivedByCentral",
        "date submitted": "name=requestSentDate",
        "method": "name=methodSent",
        "person": "name=personName",
        "person lookup": "css=img[alt='Lookup']",
        "person lookup match": "css=img[name='personLookupImage'][src$='i_match.gif']",
        "ok": "name=EditSubmittedOKEvent"
    }

    person_text = Text("person", "Text input for submitted by person")
    method = Select("method", "Method sent dropdown")
    date_received = Text("date received", "Date received (text)")
    date_submitted = Text("date submitted", "Date submitted (text)")
    submitted_by = Lookup_person(person_text, "personLookupImage", "Submitted by person lookup")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0115
        """
        return self.go("ok")
