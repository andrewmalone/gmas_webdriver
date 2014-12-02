from pages.Page import Page
from pages.elements import Text


class SCR0635(Page):
    """
    SCR_0635 Edit person jobs
    """
    locators = {
        # ac_results (div)
        "organization": "organization",
        "title": "title",
        "division": "division",
        "department": "department",
        "ok": "EditJobInfoOkEvent"
    }

    organization_text = Text("organization", "Organization edit box")
    division = Text("division", "Division")
    department = Text("department", "Department")
    title = Text("title", "Title")

    # This is an autocomplete! Needs to be added to pages.elements
    # (but probably not before UI conversion)
    @property
    def organization(self):
        """
        Organization (autocomplete)
        """
        return self.organization_text

    @organization.setter
    def organization(self, value):
        el = self.find("organization")
        el.send_keys(value)
        self.w.until(lambda d: d.find_element_by_css_selector('.ac_results').is_displayed())
        self.find_element("css=.ac_results li").click()

    def ok(self):
        """
        click <Ok>
        Goes to SCR_0025 or SCR_0252
        """
        return self.go("ok")
