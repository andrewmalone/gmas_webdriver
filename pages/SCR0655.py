from pages.Page import Page
from pages.elements import Text, Radio, Select
from selenium.webdriver.support import expected_conditions as EC


class SCR0655(Page):
    """
    SCR_0655 Inclusion enrollment
    Currently supported: Adding new studies
    Not supported: Editing existing studies, Deleting studies
    """
    locators = {
        "add": "name=studyButtonForm:addStudyBtn",
        "title": "css=[id='studyForm:editStudyPanel'] input[id^='studyForm:studyTitle']",
        "delayed_onset": "delayedOnset0",
        "existing_resource": "existingResource0",
        "clinical_trial": "clinicalTrial0",
        "phase3": "nihClinicalTrial0",
        "location": "participantsLocation0",
        "type": "enrollmentType0",
        "cell": "css=[id$=studyTable0] input[type=text]",
        "done": "studyForm:doneButton"
    }

    title = Text("title", "Study title")
    _delayed_onset = Radio("delayed_onset", "Delayed onset question")
    _type = Select("type", "Enrollment type")
    existing_resource = Radio("existing_resource", "Existing resource question")
    clinical_trial = Radio("clinical_trial", "Clinical trial question")
    phase3 = Radio("phase3", "Phase 3 question")
    location = Select("location", "location selection")
    _cell = Text("cell", "Study table cell")

    def add(self):
        """
        Click the <Add study> button
        """
        self.find("add").click()
        self.w.until(EC.element_to_be_clickable(self.get_locator(self.locators["title"])))

    def ok(self):
        """
        Click the <Done> button after editing a study
        """
        self.find("done").click()
        self.w.until(EC.invisibility_of_element_located(self.get_locator("css=[id='studyForm:editStudyPanel']")))

    @property
    def delayed_onset(self):
        """
        Delayed onset question (radio)
        """
        return self._delayed_onset

    @delayed_onset.setter
    def delayed_onset(self, val):
        self._delayed_onset = val
        if val == "false":
            self.w.until(EC.element_to_be_clickable(self.get_locator("id=studyForm:studyComments0")))

    @property
    def enrollment_type(self):
        """
        Enrollment type (select)
        """
        return self._type

    @enrollment_type.setter
    def enrollment_type(self, val):
        self._type = val
        # do the wait here
        self.w.until(EC.element_to_be_clickable(self.get_locator("css=[id$=studyTable0] input[type=text]")))

    def set_text(self, val):
        """
        Sets all study table inputs to the same value
        """
        from selenium.webdriver.common.keys import Keys
        cell_count = len(self.finds("cell"))
        for i in range(cell_count):
            cell = self.finds("cell")[i]
            cell.send_keys(Keys.BACKSPACE)
            cell.send_keys(val)
            cell.send_keys(Keys.TAB)
            self.w.until(EC.staleness_of(cell))
