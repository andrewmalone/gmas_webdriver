from pages.Page import Page
from pages.elements import Select

locators = {
    "role selection": "css=select[name='role'] option:contains('REPLACE')",
    "role": "name=role",
    "appt selection": "sizzle=select[name='appointment'] option:contains('REPLACE')",
    "name input": "name=personName",
    "name lookup": "css=img[title='Lookup']",
    "name match": "css=img[name='personLookupImage'][src*='i_match.gif']",
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

    def select_role(self, role):
        self.find_element(locators["role selection"].replace("REPLACE", role)).click()

    def lookup_huid(self, huid):
        elem = self.find_element(locators["name input"])
        elem.clear()
        elem.send_keys(huid)
        self.find_element(locators["name lookup"]).click()
        self.w.until(lambda e: self.find_element(locators["name match"]))
        # try to account for page load?
        return SCR0252(self.driver)

    def select_appt(self, appt):
        self.find_element(locators["appt selection"].replace("REPLACE", appt)).click()
        # try to account for page load...
        return SCR0252(self.driver)

    def set_human_subjects(self, val):
        self.find_element(locators["human subjects"].replace("REPLACE", val)).click()

    def set_phs(self, val):
        self.find_element(locators["PHS"].replace("REPLACE", val)).click()

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
        self.find_element(locators["ok"]).click()
        from pages.SCR0015 import SCR0015
        return SCR0015(self.driver)
