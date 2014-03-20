from pages.Page import Page


class SCR0217a(Page):
    """
    SCR_0217a Edit Organization details
    """
    locators = {
        "cancel": "EditInternalOrganizationDetailsCancelEvent"
    }

    def cancel(self):
        """
        Click <Cancel>
        Goes to SCR_0134a
        """
        return self.go("cancel")
