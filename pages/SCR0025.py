from pages.Page import Page


class SCR0025(Page):
    """
    SCR_0025 Person profile
    """
    locators = {
        "add job": "css=a[href*='EditJobInfoEvent'] img",
        "add phone": "css=a[href*='PersonProfileAddPhoneEvent'] img",
        "add email": "css=a[href*='PersonProfileAddEmailEvent'] img",
        "add address": "css=a[href*='PersonProfileAddAddressEvent'] img",
        "phones": "css=#phoneNumbersCCBODY tr:not(.bg3)",
        "addresses": "css=#addressesCCBODY tr:not(.bg3)",
        "emails": "css=#emailAddressesCCBODY tr:not(.bg3)",
        "documents": "link=Documents"
    }

    def count_phones(self):
        """
        Returns the number of phone numbers for a person
        """
        phones = self.finds("phones")
        return len(phones) - 1

    def count_emails(self):
        """
        Returns the number of email addresses for a person
        """
        emails = self.finds("emails")
        return len(emails) - 1

    def count_addresses(self):
        """
        Returns the number of addresses for a person
        """
        addresses = self.finds("addresses")
        return len(addresses) - 1

    def add_phone(self):
        """
        Click the <add> button for phone numbers
        Goes to SCR_0514
        """
        return self.go("add phone")

    def add_email(self):
        """
        Click the <add> button for email
        Goes to SCR_0470
        """
        return self.go("add email")

    def add_address(self):
        """
        Click the <add> button for address
        Goes to SCR_0411
        """
        return self.go("add address")

    def goto_documents(self):
        """
        Click the "documents" link
        Goes to SCR_0433
        """
        return self.go("documents")