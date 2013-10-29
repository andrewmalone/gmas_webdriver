# TODO: Add doc strings
from pages.Page import Page
from pages.elements import Select, Text, Radio
from pages.lookups import Lookup_person

locators = {
    "role": "name=role",
    "appt": "name=appointment",
    "name input": "name=personName",
    "human subjects": "css=[name='isMemberInvolvedWithHumanSubjects'][value='REPLACE']",
    "PHS": "css=[name='isMemberPHSInvestigator'][value='REPLACE']",
    "effort": "css=input[name$='__effort']",
    "key": "css=input[name$='__keyPersonFlag']",
    "salary": "css=input[name$='__requestedSalary']",
    "fringe": "css=input[name$='__fringeAmount']",
    "ok": "name=EditResearchPersonnelOkEvent"
}


class SCR0252(Page):
    locators = locators
    role = Select("role")
    appt = Select("appt")
    name_text = Text("name input", "Text entry field for person name")
    name = Lookup_person(name_text, 'personLookupImage', "Research team person lookup")
    human_subjects = Radio("human subjects", "Human subjects radio button")
    phs = Radio("PHS", "PHS investigator radio button")

    def _set_budget_field(self, val, elems):
        l = []
        if type(val) is int:
            l = [val for i in range(len(elems))]
        elif type(val) is list:
            l = val
            # TODO: pad the length here, if there aren't enough
        for i, elem in enumerate(elems):
            elem.clear()
            elem.send_keys(str(l[i]))
            # fire the page's javascript event to update the autocalc
            # TODO: investigate a cleaner way to handle this
            self.driver.execute_script("notifyField(arguments[0])", elem.get_attribute("name"))

    def set_human_subjects(self, val):
        self.find_element(locators["human subjects"].replace("REPLACE", val)).click()

    def set_phs(self, val):
        self.find_element(locators["PHS"].replace("REPLACE", val)).click()

    # TODO: make this cleaner (make into a descriptor?)
    def set_effort(self, val):
        self._set_budget_field(val, self.finds("effort"))

    def set_salary(self, val):
        self._set_budget_field(val, self.finds("salary"))

    def set_fringe(self, val):
        self._set_budget_field(val, self.finds("fringe"))

    def set_key(self, val):
        if val == "true":
            val = True
        else:
            val = False
        for elem in self.find_elements(locators["key"]):
            if elem.is_selected() != val:
                elem.click()

    def ok(self):
        return self.go("ok")
