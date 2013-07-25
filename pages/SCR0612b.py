from pages.Page import Page


# TODO: Check if 612 from request home should be in same page object
class SCR0612b(Page):
    """
    SCR_0612b Grants.gov questions (RGS)
    """
    locators = {
        "next": "name=CreateGrantsGovQuestionsNextEvent"
    }

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0610b
        """
        self.find("next").click()
        return self.load_page()
