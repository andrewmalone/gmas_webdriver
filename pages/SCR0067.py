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

    org_name = Text("org_name", "Text entry for new name")

    def search(self):
        """
        Clicks <Search>
        Stays on SCR0067
        """
        return self.go("search")

    def goto_first_org(self):
        return self.go("org link")
