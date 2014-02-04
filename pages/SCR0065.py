from pages.Page import Page
from pages.elements import Text


class SCR0065(Page):
    """
    SCR_0065 Person Search
    """
    locators = {
        "name": "name=fullName",
        "search": "name=PeopleSearchEvent",
        "result": "css=a[href*='PersonNameLinkEvent']",
        "teams": "link=GMAS Teams"
    }

    name = Text("name", "Edit box for name/HUID")

    def nav_to(self):
        """
        Direct navigation to person search
        """
        # TODO: Make global nav stuff available to every page
        url = "https://%s.harvard.edu/gmas/dispatch?ref=%%2Fcommon%%2FCOM0100GlobalNavigation.jsp&refreshBreadCrumbs=true&formName=linker&GoPeopleEvent=" % self.env
        self.driver.get(url)
        return self.load_page()

    def search(self):
        """
        Click the <search> button
        Returns a new page object
        """
        return self.go("search")

    def click_first_result(self):
        """
        Clicks the first result.
        Goes to SCR_0025
        """
        return self.go("result")

    def goto_teams(self):
        """
        Click the "GMAS Teams" link
        Goes to SCR_0066
        """
        return self.go("teams")