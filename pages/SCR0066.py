from pages.Page import Page
from pages.elements import Text, Row


class SCR0066(Page):
    """
    SCR_0066 Team search
    """
    locators = {
        "name": "teamName",
        "search": "TeamSearchEvent",
        "row": "xpath=//a[contains(@href,'TeamManagerEvent')]/ancestor::tr[1]",
        "row_name": "xpath=//a[normalize-space(text())='REPLACE']/ancestor::tr[1]"
    }

    name = Text("name", "Team name")

    def search(self):
        """
        Click <Search>
        """
        return self.go("search")

    def row(self, identifier):
        """
        Returns a search result row based on number (1 indexed) or name (exact match)
        //Result_row
        """
        if type(identifier) is int:
            row = self.finds("row")[identifier - 1]
            
        if type(identifier) is str:
            row = self.find("row_name", identifier.strip())

        return self.Result_row(row, self)

    
    class Result_row(Row):
        locators = {
            "link": "css=a[href*=TeamManagerEvent]"
        }

        def go(self):
            """
            Click the standing team link
            Goes to SCR_0050
            """
            return self._go("link")

