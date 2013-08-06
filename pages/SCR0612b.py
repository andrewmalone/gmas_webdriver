from pages.Page import Page


class PS_Element(object):
    def __init__(self, label, doc):
        self.label = label
        self.__doc__ = doc

    def find(self, obj):
        locator = "css=[name$='__questionDescription'][value='%s']" % self.label
        elem = obj.find_elements(locator)[-1]
        name = elem.get_attribute("name").replace("__questionDescription", "__textResponse")
        locator = "name=%s" % name
        return obj.find_element(locator)


class PS_Text(PS_Element):
    def __set__(self, obj, val):
        elem = self.find(obj)
        elem.clear()
        elem.send_keys(val)

    def __get__(self, obj, type=None):
        pass


class PS_Select(PS_Element):
    def __set__(self, obj, val):
        from selenium.webdriver.support.select import Select as WDSelect
        elem = WDSelect(self.find(obj))
        elem.select_by_visible_text(val)

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

    ps_organization_name = PS_Text("Organization Name:", "Performance site organization name (text)")
    ps_duns = PS_Text("DUNS Number:", "Performance site DUNS (text)")
    ps_street1 = PS_Text("Street 1:", "Performance site Street 1 (text)")
    ps_street2 = PS_Text("Street 2:", "Performance site Street 2 (text)")
    ps_city = PS_Text("City:", "Performance site City (text entry)")
    ps_county = PS_Text("County:", "Performance site County (text entry)")
    ps_state = PS_Select("State:", "Performance site State (dropdown)")
    ps_province = PS_Text("Province:", "Performance site Province (text)")
    ps_zip = PS_Text("Zip Code:", "Performance site zip code (text)")
    ps_country = PS_Select("Country:", "Performance site country (dropdown)")
    ps_district = PS_Text("Site Congressional District:", "Performance site congressional district (text)")

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
