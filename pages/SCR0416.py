from pages.Page import Page


class SCR0416(Page):
    """
    SCR_0416 Add roles to admin team
    """
    locators = {
        "checkbox": "xpath=//input[@value='REPLACE']/ancestor::tr[1]//input[@type='checkbox']",
        "next": "partial=Next",
        "ok": "SelectRolesOKEvent"
    }

    def select_role(self, role):
        """
        Clicks the checkbox next to the specified role
        """
        self.find("checkbox", role).click()

    def has_role(self, role):
        """
        returns True or False depending on whether the role is currently present on the page
        """
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.find("checkbox", role)
        except NoSuchElementException:
            return False

        return True

    def next(self):
        """
        Click the "next" link to go to the next page of roles
        """
        return self.go("next")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0300
        """
        return self.go("ok")
