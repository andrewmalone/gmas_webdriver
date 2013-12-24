from pages.Page import Page


class SCR0232(Page):
    """
    SCR_0232 Subagreement List
    """
    locators = {
        "subagreement link": "css=a[href*='ViewSubagreementEvent']"        
    }

    def goto_first_subagreement(self):
        """
        Clicks the first subagreement link on the page
        Goes to SCR_0450 or SCR_0233
        """
        return self.go("subagreement link")

    
