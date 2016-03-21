from pages.Page import Page


class Q_Element(object):
    def __init__(self, id, doc):
        self.id = id
        self.__doc__ = doc

    def find(self, obj):
        locator = "css=[name$='__questionId'][value='%s']" % self.id
        elem = obj.find_elements(locator)[-1]
        name = elem.get_attribute("name").replace("__questionId", "__textResponse")
        locator = "name=%s" % name
        return obj.find_element(locator)


class Q_Text(Q_Element):
    def __set__(self, obj, val):
        elem = self.find(obj)
        elem.clear()
        elem.send_keys(val)

    def __get__(self, obj, type=None):
        pass


class Q_Select(Q_Element):
    def __set__(self, obj, val):
        from selenium.webdriver.support.select import Select as WDSelect
        elem = WDSelect(self.find(obj))
        elem.select_by_visible_text(val)

    def __get__(self, obj, type=None):
        pass

class Q_Radio(object):
    def __init__(self, id, doc):
        self.id = id
        self.__doc__ = doc

    def __set__(self, obj, val):
        locator = "css=input[name='radioResponse_%s']" % self.id
        radios = obj.find_elements(locator)
        radios[val - 1].click()


    def __get__(self, obj, type=None):
        pass

class SCR0612b(Page):
    """
    SCR_0612b Grants.gov questions (RGS)
    {note}
    All performance site descriptors will select the last available performance site
    {note}
    """
    locators = {
        "next": "name=CreateGrantsGovQuestionsNextEvent",
        "ok": "name=EditGrantsGovQuestionsOKEvent",
        "add ps": "css=input[onclick*='sendAdditionalGroupId(\\'1\\')']"
    }

    sf424_1 = Q_Text(3287353, "Federal Identifier (text)")
    sf424_2 = Q_Text(3287354, "Agency Routing number (text)")
    sf424_3 = Q_Radio(3287356, "Revision application (radio)")
    sf424_4 = Q_Radio(3287359, "Other agencies? (radio)")
    sf424_4a = Q_Text(3287361, "Other agency (text)")
    sf424_5b = Q_Text(3287366, "Total non-federal funds (text)")
    sf424_6 = Q_Radio(3287368, "State executive order (radio)")
    sf424_6a = Q_Text(3287370, "Review date (text)")

    rr_other_1 = Q_Radio(3158590, "Proprietary/priveleged info (radio)")
    rr_other_2 = Q_Radio(3158593, "Environmental imact (radio")
    rr_other_2a = Q_Text(3158595, "Environmental explanation (text)")
    rr_other_2b = Q_Radio(3158596, "Environmental exception (radio)")
    rr_other_2c = Q_Text(3158598, "Environmental exception explanation (text)")
    rr_other_3 = Q_Radio(3158601, "Historic site (radio)")
    rr_other_3a = Q_Text(3158603, "Historic site explanation (text)")
    rr_other_4 = Q_Radio(3158605, "International activities (radio)")
    rr_other_4a = Q_Text(3158607, "Identify countries (text)")
    rr_other_4b = Q_Text(3158608, "International explanation (text)")

    ps_organization = Q_Text(3300710,"Performance site organization name (text)")
    ps_duns = Q_Text(3300711, "Performance site DUNS (text)")
    ps_street1 = Q_Text(3300712, "Performance site Street 1 (text)")
    ps_street2 = Q_Text(3300713, "Performance site Street 2 (text)")
    ps_city = Q_Text(3300714, "Performance site City (text)")
    ps_county = Q_Text(3300715, "Performance site County (text)")
    ps_state = Q_Select(3300716, "Performance site State (dropdown)")
    ps_province = Q_Text(3300717, "Performance site Province (text)")
    ps_zip = Q_Text(3300718, "Performance site zip code (text)")
    ps_country = Q_Select(3300719,"Performance site country (dropdown)")
    ps_district = Q_Text(3300720, "Performance site congressional district (text)")

    ###
    # Cover page supplement 3.0
    ###
    phs_cover_1a1 = Q_Radio(3300302, "Clinical trial (radio)")
    phs_cover_1a2 = Q_Radio(3300305, "Phase III Clinical trial (radio)")
    phs_cover_2a1 = Q_Radio(3300309, "Vertebrate animals euthanized (radio)")
    phs_cover_2a2 = Q_Radio(3300312, "AVMA guidelines (radio)")
    phs_cover_2a3 = Q_Text(3300315, "Scientific justification (text)")
    phs_cover_cell_line = Q_Text(3300320, "Cell line (text)")
    # TODO - add checkbox!
    phs_cover_4 = Q_Radio(3300322, "Inventions and Patents (radio)")
    phs_cover_4a = Q_Radio(3300325, "Inventions previously reported (radio)")
    phs_cover_5 = Q_Radio(3300328, "Change of investigator (radio)")
    phs_cover_5a_prefix = Q_Select(3300331, "Prefix (dropdown)")
    phs_cover_5a_firstname = Q_Text(3300332, "First name (text)")
    phs_cover_5a_middlename = Q_Text(3300333, "Middle name (text)")
    phs_cover_5a_lastname = Q_Text(3300334, "Last name (text)")
    phs_cover_5a_suffix = Q_Select(3300335, "Suffix (dropdown)")
    phs_cover_6 = Q_Radio(3300337, "Change of institution (radio)")
    phs_cover_6a = Q_Text(3300339, "Institution name (text)")

    ###
    # These are the 2.0 question definitions
    ###
    # phs_cover_1a1 = Q_Radio(3301625, "Clinical trial (radio)")
    # phs_cover_1a2 = Q_Radio(3301628, "Phase III Clinical trial (radio)")
    # phs_cover_2 = Q_Radio(3301663, "Disclosure permission (radio)")
    # phs_cover_cell_line = Q_Text(3301640, "Cell line (text)")
    # # TODO - add checkbox!
    # phs_cover_4 = Q_Radio(3301668, "Inventions and Patents (radio)")
    # phs_cover_4a = Q_Radio(3301670, "Inventions previously reported (radio)")
    # phs_cover_5 = Q_Radio(3301648, "Change of investigator (radio)")
    # phs_cover_5a_prefix = Q_Select(3301650, "Prefix (dropdown)")
    # phs_cover_5a_firstname = Q_Text(3301651, "First name (text)")
    # phs_cover_5a_middlename = Q_Text(3301652, "Middle name (text)")
    # phs_cover_5a_lastname = Q_Text(3301653, "Last name (text)")
    # phs_cover_5a_suffix = Q_Select(3301654, "Suffix (dropdown)")
    # phs_cover_6 = Q_Radio(3301655, "Change of institution (radio)")
    # phs_cover_6a = Q_Text(3301656, "Institution name (text)")

    fellowship_4c = Q_Select(3301530, "Field of study (dropdown)")
    fellowship_4d = Q_Radio(3301531, "Prior support (radio)")
    fellowship_4e = Q_Radio(3301542, "concurrent support (radio)")
    fellowship_4f = Q_Radio(3301545, "Citizenship (radio)")
    fellowship_5 = Q_Radio(3301553, "Change of institution (radio)")
    fellowship_6a = Q_Radio(3301559, "Tuition and fees (radio)")

    career_1 = Q_Radio(3301696, "Citizenship (radio)")
    career_1a = Q_Radio(3301699, "Citizenship subquestion (radio)")
    career_1b = Q_Select(3301703, "Citizenship visa (select)")

    assign_award1 = Q_Text(3301707, "Assign to Awarding Component (1) (text)")
    assign_award2 = Q_Text(3301708, "Assign to Awarding Component (2) (text)")
    assign_award3 = Q_Text(3301709, "Assign to Awarding Component (3) (text)")
    assign_award4 = Q_Text(3301710, "Do not Assign to Awarding Component (1) (text)")
    assign_award5 = Q_Text(3301711, "Do not Assign to Awarding Component (2) (text)")
    assign_award6 = Q_Text(3301712, "Do not Assign to Awarding Component (3) (text)")
    assign_study1 = Q_Text(3301717, "Assign to Study Section (1) (text)")
    assign_study2 = Q_Text(3301718, "Assign to Study Section (2) (text)")
    assign_study3 = Q_Text(3301719, "Assign to Study Section (3) (text)")
    assign_study4 = Q_Text(3301720, "Do not Assign to Study Section (1) (text)")
    assign_study5 = Q_Text(3301721, "Do not Assign to Study Section (2) (text)")
    assign_study6 = Q_Text(3301722, "Do not Assign to Study Section (3) (text)")
    assign_individuals = Q_Text(3301724, "Individuals not to assign (text)")
    assign_expertise1 = Q_Text(3301727, "Expertise (1) (text)")
    assign_expertise2 = Q_Text(3301728, "Expertise (2) (text)")
    assign_expertise3 = Q_Text(3301729, "Expertise (3) (text)")
    assign_expertise4 = Q_Text(3301730, "Expertise (4) (text)")
    assign_expertise5 = Q_Text(3301731, "Expertise (5) (text)")

    def add_ps(self):
        """
        Click the <Add> button for performance site (returns a new page object)
        """
        return self.go("add ps")

    def ok(self):
        """
        Click <Next> or <Ok>
        Goes to SCR_0610b or SCR_0115
        Returns a new page object
        """
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.find("next").click()
        except NoSuchElementException:
            self.find("ok").click()
        return self.load_page()

