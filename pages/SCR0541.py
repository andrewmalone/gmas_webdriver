from pages.Page import Page
from pages.elements import Checkbox


class SCR0541(Page):
    """
    SCR_0541 Select changes to existing segment
    """
    locators = {
        "preaward": "css=input[name='requestSubTypeId'][value='5007']",
        "carryforward": "css=input[name='requestSubTypeId'][value='5008']",
        "nocost": "css=input[name='requestSubTypeId'][value='5009']",
        "equipment": "css=input[name='requestSubTypeId'][value='5010']",
        "sub": "css=input[name='requestSubTypeId'][value='5011']",
        "ifi": "css=input[name='requestSubTypeId'][value='5012']",
        "changepi": "css=input[name='requestSubTypeId'][value='5013']",
        "rebudget": "css=input[name='requestSubTypeId'][value='5014']",
        "termination": "css=input[name='requestSubTypeId'][value='5015']",
        "next": "SelectChangesToExistingSegmentNextEvent"
    }

    preaward = Checkbox("preaward", "Pre-award expenditure")
    carryforward = Checkbox("carryforward", "Carryforward")
    nocost = Checkbox("nocost", "No-cost extension")
    equipment = Checkbox("equipment", "Equipment rebudget")
    sub = Checkbox("sub", "Sub at no cost")
    ifi = Checkbox("ifi", "Ifi at no cost")
    changepi = Checkbox("changepi", "Change PI")
    rebudget = Checkbox("rebudget", "Rebudget restricted categories")
    termination = Checkbox("termination", "Early termination")

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0465
        """
        return self.go("next")
