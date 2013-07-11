from pages.Page import Page
from pages.elements import Text, Select


class SCR0401(Page):
    locators = {
        "date received": "name=dateReceivedByCentral",
        "date submitted": "name=requestSentDate",
        "method": "name=methodSent",
        "person": "name=personName",
        "person lookup": "css=img[alt='Lookup']",
        "person lookup match": "css=img[name='personLookupImage'][src$='i_match.gif']",
        "ok": "name=EditSubmittedOKEvent"
    }

    class Lookup_person(object):
        def __set__(self, obj, val):
            obj.lookup_person(val)

    person_text = Text("person")
    method = Select("method")
    date_received = Text("date received")
    date_submitted = Text("date submitted")
    submitted_by = Lookup_person()

    def lookup_person(self, huid):
        self.person_text = huid
        self.find("person lookup").click()
        self.w.until(lambda e: self.find("person lookup match"))
        return self

    def ok(self):
        return self.go("ok")
