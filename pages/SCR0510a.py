from pages.Page import Page


class SCR0510a(Page):
    """
    SCR_0510a Edit organization signatures
    """
    locators = {
        "cancel": "OrganizationSignatureRulesCancelEvent"
    }

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0134a
        """
        return self.go("cancel")
