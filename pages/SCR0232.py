from pages.Page import Page


class SCR0232(Page):
    """
    SCR_0232 Subagreement List
    """
    locators = {
        "subagreement link": "css=a[href*='ViewSubagreementEvent']"        
    }

    def goto_first_subagreement(self):
        return self.go("subagreement link")

    
