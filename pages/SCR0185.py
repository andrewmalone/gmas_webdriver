from pages.Page import Page
from pages.elements import Select

a21_map = {
    "A01": "A01-Instruction & Training",
    "A02": "A02-Organized Research",
    "A03": "A03-Other Sponsored Activities",
    "A15": "A15-Scholarships & Student Aid"
}

class SCR0185(Page):
    """
    SCR_0185 Create new activity
    """
    locators = {
        "a21": "a21FunctionalCode",
        "ok": "CreateActivityOKEvent",
        "get": "GetNewActivityForCreateEvent"
    }

    a21 = Select("a21", "A-21 code", a21_map)

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0182
        """
        return self.go("ok")