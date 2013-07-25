from pages.Page import Page
from pages.elements import Select, Text


class Lookup_person(object):
    """
    Enters an HUID into the text box and does the lookup (needs an HUID)
    """
    def __set__(self, obj, val):
        obj.name_input = val
        obj.find("name lookup").click()
        obj.w.until(lambda e: obj.find("name lookup match"))

    def __get__(self, obj, type=None):
        pass


class SCR0230(Page):
    """
    SCR_0230 Add to admin team in RGS
    """
    locators = {
        "role": "name=listBuilderRoleId",
        "name input": "name=listBuilderPersonName",
        "name lookup": "css=a[href*='piImage'] img",
        "name lookup match": "css=img[name='piImage'][src*='i_match.gif']",
        "ok": "name=GrantsMgmtTeamBuilderOKEvent"
    }

    role = Select("role", "Role dropdown (needs exact text match)")
    name_input = Text("name input", "Text input for name")
    name = Lookup_person()

    def ok(self):
        return self.go("ok")
