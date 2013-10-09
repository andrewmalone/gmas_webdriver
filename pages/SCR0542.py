from pages.Page import Page
from pages.elements import Checkbox


class SCR0542(Page):
    """
    SCR_0542 Select internal request type
    """
    locators = {
        "next": "name=SelectInternalRequestNextEvent",
        "new account": "css=input[name='requestSubTypeId'][value='5016']",
        "at-risk account": "css=input[name='requestSubTypeId'][value='5017']",
        "change tub/org": "css=input[name='requestSubTypeId'][value='5018']"
    }

    new_acct = Checkbox("new account", "Checkbox for new account type")
    atrisk_acct = Checkbox("at-risk account", "Checkbox for at-risk account type")
    change_tub = Checkbox("change tub/org", "Check box for change Tub/Org type")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0465
        """
        return self.go("next")