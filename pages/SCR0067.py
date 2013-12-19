from pages.Page import Page
from pages.elements import Text

class SCR0067(Page):
    """
    SCR_0067 Organization search
    """
    locators = {
        "org_name": "name=organizationSearchString",
        "search": "name=MainOrganizationSearchEvent",
        "org link": "css=a[href*='ViewOrganizationDetailsEvent']"
    }

    org_name = Text("org_name", "Organization name")

    def search(self):
        """
        Clicks <Search>
        """
        return self.go("search")

    def goto_first_org(self):
        """
        Clicks the first search result
        Goes to SCR_0134a or SCR_0134b
        """
        return self.go("org link")
