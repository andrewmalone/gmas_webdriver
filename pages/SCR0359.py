from pages.Page import Page
from pages.elements import Text, RText, Row


class SCR0359(Page):
    """
    SCR_0359 Edit dates in revision
    """
    locators = {
        "ob_start": "css=[name$='obligatedStartDate']",
        "ob_end": "css=[name$='obligatedEndDate']",
        "periods": "css=input[name$=awardedDateVersion]+tr+tr",
        "next": "name=EditPeriodDatesNextEvent",
        "done": "name=EditPeriodDatesDoneEvent"
    }

    ob_start = Text("ob_start", "Obligated start date")
    ob_end = Text("ob_end", "Obligated end date")

    @property
    def period_count(self):
        """
        Number of periods
        """
        return len(self.finds("periods"))

    def period(self, n):
        """
        Returns the nth period row
        //PeriodRow
        """
        row = self.finds("periods")[n - 1]
        return self.PeriodRow(row, self)

    def next(self):
        """
        Click <Next>
        Goes to SCR_0123
        """
        return self.go("next")

    def done(self):
        """
        Click <Done making revisions to this section>
        Goes to SCR_0105
        """
        return self.go("done")

    class PeriodRow(Row):
        locators = {
            "period": "css=td:nth-child(2)",
            "proposed start": "css=td:nth-child(6)",
            "proposed end": "css=td:nth-child(10)",
            "ob_start": "css=[name$='obligatedStartDate']",
            "ob_end": "css=[name$='obligatedEndDate']",
            "ant_start": "css=[name$='anticipatedStartDate']",
            "ant_end": "css=[name$='anticipatedEndDate']"
        }

        period_number = RText("period", "budget period number")
        proposed_start = RText("proposed start", "Proposed start date")
        proposed_end = RText("proposed end", "Proposed end date")
        ob_start = Text("ob_start", "Obligated start date")
        ob_end = Text("ob_end", "Obligated end date")
        ant_start = Text("ant_start", "Anticipated start date")
        ant_end = Text("ant_end", "Anticipated end date")
