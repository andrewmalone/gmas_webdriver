from pages.Page import Page


class SCR0615a(Page):
    """
    SCR_0615a Grants.gov preview/validate
    """
    locators = {
        "select all": "css=img[title='Select all']",
        "validate": "PreviewGrantsGovValidateEvent",
        "preview": "PreviewGrantsGovFormEvent"
    }

    def select_all(self):
        """
        Click <Select all>
        """
        self.find("select all").click()

    def validate(self):
        """
        Click <Validate>
        Goes to SCR_0615b
        """
        return self.go("validate")

    def preview(self):
        """
        Click <Preview>
        """
        self.find("preview").click()
