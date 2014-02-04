from pages.Page import Page


class SCR0301(Page):
    """
    SCR_0301 Project Admin Role
    """
    locators = {
        "input": "xpath=//td[contains(text(),'REPLACE')]/ancestor::tr[1]//input",
        "remove": "RemoveSelectedPeopleFromRoleEvent",
        "add": "AddPersonToRoleEvent"
    }

    def add(self):
        """
        Click <Add person to role>
        Goes to SCR_0051
        """
        return self.go("add")

    def remove(self):
        """
        Click <Remove selected people from role>
        """
        return self.go("remove")

    def select_name(self, name):
        """
        Selects a checkbox next to one of the names
        **note**: person id or huid are not available on this page, name is the best we can do for now
        """
        self.find("input", name).click()