
from pages.Page import Page


class SCR0227(Page):
    locators = {
        "next": "name=RequestPeriodDatesNextEvent",
        "period start": "css=[name$='REPLACE__periodStartDate']"
    }

    def set_period_start(self, period, start):
        elem = self.find("period start", int(period) - 1)
        elem.send_keys(start)

    def calc_periods(self, start, periods):
        from datetime import datetime, date
        start = datetime.strptime(start, "%m/%d/%y")
        for i in range(1, int(periods)):
            per_start = date.strftime(date(start.year + i, start.month, start.day), "%m/%d/%y")
            self.set_period_start(i+1, per_start)
        return self

    def ok(self):
        self.find("next").click()
        # will be SCR0229
        return self.load_page()
