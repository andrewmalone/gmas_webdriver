from pages.Page import Page
from pages.elements import Radio


class SCR0461(Page):
    """
    SCR_0461 Edit SNAP questions
    """
    locators = {
        "next": "SnapQuestionsNextEvent",
        "q1": "css=input[name$='0__userResponse']",
        "q2": "css=input[name$='1__userResponse']",
        "q3": "css=input[name$='2__userResponse']"
    }

    q1 = Radio("q1", "SNAP Question 1")
    q2 = Radio("q2", "SNAP Question 2")
    q3 = Radio("q3", "SNAP Question 3")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0097
        """
        return self.go("next")
