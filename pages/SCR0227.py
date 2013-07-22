
from pages.Page import Page


class SCR0227(Page):
    """
    SCR_0227 Request period dates
    """
    locators = {
        "next": "name=RequestPeriodDatesNextEvent",
        "period start": "css=[name$='REPLACE__periodStartDate']"
    }

    def set_period_start(self, period, start_date):
        """
        Enters the start date for an individual period
        *Example:* set_period_start(3, '3/1/13') sets period 3 start date to 3/1/13
        """
        elem = self.find("period start", int(period) - 1)
        elem.send_keys(start_date)

    def calc_periods(self, start_date, number_of_periods):
        """
        Helper methods - based on the request start date and the total number of periods, enter the start date for all periods. This assumes 1 year budget periods.

        *Example*: calc_periods('6/1/08', 3) sets the following dates:
        * Period 2 - 6/1/09
        * Period 3 - 6/1/10

        (!) Note that end dates are not entered onto this screen
        """
        from datetime import datetime, date
        start = datetime.strptime(start_date, "%m/%d/%y")
        for i in range(1, int(number_of_periods)):
            per_start = date.strftime(date(start.year + i, start.month, start.day), "%m/%d/%y")
            self.set_period_start(i+1, per_start)
        return self

    def ok(self):
        """
        Click <Next>
        Goes to SCR_0229
        """
        self.find("next").click()
        return self.load_page()
