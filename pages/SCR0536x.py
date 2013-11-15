# POPUP screen!
from pages.Page import Page
from pages.elements import Select, Text


class SCR0536x(Page):
    """
    SCR_0536x Organization search popup
    """
    locators = {
        "organization": "name=organizationSearchString",
        "organization type": "name=organizationTypeString",
        "search": "name=OrganizationLookupxEvent",
        "first result": "name=concatenatedOrganization",
        "ok": "name=OrganizationSearchOkEvent"
    }

    organization_type = Select("organization type", "Dropdown for organization type")
    name = Text("organization", "Text entry for organization name")

    def search(self):
        return self.go("search")

    def select_first_result(self):
        # why is this here? I don't remember!
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.find("first result").click()
        except NoSuchElementException:
            print "error!"
            self.find("first result").click()

    def ok(self):
        self.find("ok").click()
        # return to the main window
        self.driver.switch_to_window(self.driver.window_handles[0])
