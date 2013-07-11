from pages.Page import Page
from pages.elements import Text


class SCR0090(Page):
    locators = {
        "start": "name=requestStartDate",
        "end": "name=requestEndDate",
        "periods": "name=numberOfPeriods",
        "next": "name=RequestDatesNextEvent"
    }

    start = Text("start")
    end = Text("end")
    periods = Text("periods")

    def calc_end(self, start, periods):
        from datetime import datetime, date, timedelta
        start = datetime.strptime(start, "%m/%d/%y")
        end = date.strftime(date(start.year + int(periods), start.month, start.day) - timedelta(days=1), "%m/%d/%y")
        self.end = end
        return self

    def ok(self):
        self.find("next").click()
        from pages.SCR0227 import SCR0227
        return SCR0227(self.driver)
