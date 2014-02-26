from pages.Page import Page
from pages.elements import Row

class SCR0344(Page):
    """
    SCR_0344 Request list
    """
    locators = {
        "request row": "xpath=//a[contains(@href,'RequestListLinkEvent')]/ancestor::tr[1]"
    }

    def requests(self, num):
        """
        returns a request row based on the num index (1 indexed)
        //request_row
        """
        return self.request_row(self.finds("request row")[num - 1], self)


    class request_row(Row):
        locators = {
            "link": "css=a[href*=RequestListLinkEvent]"
        }

        def go(self):
            """
            Clicks the request link
            Goes to SCR_0115
            """
            return self._go("link")