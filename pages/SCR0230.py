from pages.Page import Page
from pages.elements import Select, Text
from pages.lookups import Lookup_person


class SCR0230(Page):
    """
    SCR_0230 Add to admin team in RGS
    """
    locators = {
        "role": "name=listBuilderRoleId",
        "name input": "name=listBuilderPersonName",
        "ok": "name=GrantsMgmtTeamBuilderOKEvent"
    }

    role = Select("role", "Role dropdown (needs exact text match)")
    name_input = Text("name input", "Text input for name")
    name = Lookup_person(name_input,"piImage","Admin team person lookup")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0099
        """
        return self.go("ok")
