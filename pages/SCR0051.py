from pages.Page import Page
from pages.elements import Text


class SCR0051(Page):
    """
    SCR_0051 Person search
    """
    locators = {
        "name": "fullName",
        "search": "PeopleSearchEvent",
        "ok": "PeopleSelectOkEvent",
        "result": "concatenatedSelectedPersonString"
    }

    name = Text("name", "Name/HUID")

    def search(self):
        """
        Click <search>
        """
        return self.go("search")

    def select_first(self):
        """
        Select the first result
        """
        self.find("result").click()

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0050 (and others)
        """
        return self.go("ok")