from pages.Page import Page
from pages.elements import Text


class SCR0090(Page):
    """
    SCR_0090 Enter request dates
    """
    locators = {
        "start": "name=requestStartDate",
        "end": "name=requestEndDate",
        "periods": "name=numberOfPeriods",
        "next": "name=RequestDatesNextEvent",
        "cancel": "RequestDatesCancelEvent"
    }

    start = Text("start", "text input for start date")
    end = Text("end", "text input for end date")
    periods = Text("periods", "text input for number of periods")

    def calc_end(self, start_date, num_periods):
        """
        helper method - sets the end date field based on the start date and the number of periods (assumes 1 year period)
        example: calc_end("6/1/08", 2) would set the end date to 5/30/10
        """
        from datetime import datetime, date, timedelta
        start = datetime.strptime(start_date, "%m/%d/%y")
        end = date.strftime(date(start.year + int(num_periods), start.month, start.day) - timedelta(days=1), "%m/%d/%y")
        self.end = end
        return self

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0227
        """
        self.find("next").click()
        from pages.SCR0227 import SCR0227
        return SCR0227(self.driver)

    def cancel(self):
        """
        Clicks <Cancel>
        Goes to SCR_0270 (for initial)
        """
        return self.go("cancel")
