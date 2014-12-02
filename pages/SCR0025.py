from pages.Page import Page
import utilities.xpath as xpath
from pages.elements import RText


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
        "credentials": "css=#agencyCredentialsCCBODY tr:not(.bg3)",
        "add credential": "css=a[href*='PersonProfileAddCredentialEvent'] img",
        "documents": "link=Documents",
        "edit": "css=a[href*='PersonProfileEditEvent'] img",
        "user_flag": xpath.text_sibling("td", "GMAS user", 2),
        "huid": xpath.text_sibling("td", "University ID", 4),
        "name": xpath.text_sibling("td", "Full name", 4),
        "standing team": "xpath=//a[contains(@href,'PersonProfileViewTeamEvent')][contains(text(),'REPLACE')]",
        "open all": "link=open all",
        "PI dashboard": "event=ViewPIDashboardEvent"
    }

    huid = RText("huid", "HUID")
    user_flag = RText("user_flag", "GMAS User Flag")
    full_name = RText("name", "Full name (last, first middle)")

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

    def count_credentials(self):
        """
        Returns the number of agency credentials for a person
        """
        credentials = self.finds("credentials")
        return len(credentials) - 2

    def add_credential(self):
        """
        Click the <add> button for agency credentials
        Goes to SCR_0629
        """
        return self.go("add credential")

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

    def add_job(self):
        """
        Click the <add> button for jobs
        Goes to SCR_0635
        """
        return self.go("add job")

    def goto_documents(self):
        """
        Click the "documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def edit_user(self):
        """
        Click the <edit> button for person information
        Goes to SCR_0026
        """
        return self.go("edit")

    def get_person_id(self):
        """
        Gets the person id
        """
        import urlparse
        url = urlparse.urlparse(self.driver.current_url)
        query = urlparse.parse_qs(url.query)
        return query["personId"][0]

    def open_all(self):
        """
        Clicks "Open all"
        """
        self.find("open all").click()

    def goto_standing_team(self, team):
        """
        Clicks on a standing team link (based on the team name)
        Goes to SCR_0050
        """
        return self.go("standing team", team)

    def goto_pi_dashboard(self):
        """
        Clicks the "PI Dashboard" link
        Goes to SCR_0646]
        """
        return self.go("PI dashboard")