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
        locator = "css=input[parent='radioResponse_%s']" % self.id
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

    sf424_1 = Q_Text(3287353,"Federal Identifier (text)")
    sf424_2 = Q_Text(3287354,"Agency Routing number (text)")
    sf424_3 = Q_Radio(3287355,"Revision application (radio)")
    sf424_4 = Q_Radio(3287359,"Other agencies? (radio)")
    sf424_4a = Q_Text(3287361,"Other agency (text)")
    sf424_5b = Q_Text(3287366,"Total non-federal funds (text)")
    sf424_6 = Q_Radio(3287368,"State executive order (radio)")
    sf424_6a = Q_Text(3287370,"Review date (text)")

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

