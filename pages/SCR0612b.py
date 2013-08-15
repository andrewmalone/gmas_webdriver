from pages.Page import Page


class Q_Element(object):
    def __init__(self, label, doc):
        self.label = label
        self.__doc__ = doc

    def find(self, obj):
        locator = "css=[name$='__questionDescription'][value='%s']" % self.label
        elem = obj.find_elements(locator)[-1]
        name = elem.get_attribute("name").replace("__questionDescription", "__textResponse")
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
    def __init__(self, label, doc):
        self.label = label
        self.__doc__ = doc

    def __set__(self, obj, val):
        locator = "css=[name$='__questionDescription'][value='%s']" % self.label
        elem = obj.find_element(locator)
        name = elem.get_attribute("name").replace("__questionDescription", "__questionId")
        locator = "name=%s" % name
        q_id = obj.find_element(locator).get_attribute("value")
        locator = "css=input[parent='radioResponse_%s']" % q_id
        radios = obj.find_elements(locator)
        radios[val].click()


    def __get__(self, obj, type=None):
        pass


# TODO: Check if 612 from request home should be in same page object
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

    sf424_revision = Q_Radio("3. Is this a revision application?", "test")
    sf424_other = Q_Radio("4. Is this application being submitted to other agencies/sponsors?", "test")
    sf424_nonfed = Q_Text("5b.  Total non-federal funds", "test")
    sf424_exec = Q_Radio("6. Is the application subject to review by state executive order 12372 process?", "test")

    ps_organization_name = Q_Text("Organization Name:", "Performance site organization name (text)")
    ps_duns = Q_Text("DUNS Number:", "Performance site DUNS (text)")
    ps_street1 = Q_Text("Street 1:", "Performance site Street 1 (text)")
    ps_street2 = Q_Text("Street 2:", "Performance site Street 2 (text)")
    ps_city = Q_Text("City:", "Performance site City (text entry)")
    ps_county = Q_Text("County:", "Performance site County (text entry)")
    ps_state = Q_Select("State:", "Performance site State (dropdown)")
    ps_province = Q_Text("Province:", "Performance site Province (text)")
    ps_zip = Q_Text("Zip Code:", "Performance site zip code (text)")
    ps_country = Q_Select("Country:", "Performance site country (dropdown)")
    ps_district = Q_Text("Site Congressional District:", "Performance site congressional district (text)")

    def add_ps(self):
        """
        Click the <Add> button for performance site (returns a new page object)
        """
        return self.go("add ps")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0610b or SCR_0115
        Returns a new page object
        """
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.find("next").click()
        except NoSuchElementException:
            self.find("ok").click()
        return self.load_page()
