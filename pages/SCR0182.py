from pages.Page import Page
from pages.elements import Radio

class SCR0182(Page):
    """
    SCR_0182 Select Activity
    """
    locators = {
        "create": "css=img[title='Create New Activity Value']",
        "ok": "css=img[title='OK']",
        "cancel": "css=img[title='Cancel']",
        "activity": "css=[name='row_num']"
    }

    activity = Radio("activity", "Activity selection - use integer values: `p.activity = 1`")

    def create(self):
        """
        Click <Create activity>
        Goes to SCR_0185
        """
        return self.go("create")

    def cancel(self):
        """
        Click <Cancel>
        Closes the popup and returns to SCR_0474
        """
        self.find("cancel").click()
        self.driver.switch_to_window(self.driver.window_handles[0])
        return self.load_page()

    def ok(self):
        """
        Click <Ok>
        Closes the popup and returns to SCR_0474
        """
        self.find("ok").click()
        self.driver.switch_to_window(self.driver.window_handles[0])
        return self.load_page()