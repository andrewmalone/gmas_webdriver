from pages.Page import Page
from pages.elements import Row, Text


class SCR0017(Page):
    """
    SCR_0017 Edit subagreement budget
    """
    locators = {
        "ok": "EditSubagreementBudgetOkEvent",
        "line item row": "xpath=//input[contains(@name,'zzsubagreementBudgetData')]/ancestor::tr[1]"
    }

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0006 (more, I think)
        """
        return self.go("ok")

    @property
    def line_count(self):
        """
        Count of line items
        """
        return len(self.finds("line item row"))

    def line(self, n):
        """
        Returns a line item row
        //Line_item
        """
        row = self.finds("line item row")[n - 1]
        return self.Line_item(row, self)

    class Line_item(Row):
        locators = {
            "input": "css=input[type=text][name*=zzsubagreementBudgetData]"
        }

        def enter(self, period, amount):
            elem = self.finds("input")[period - 1]
            elem.clear()
            elem.send_keys(amount)
            script = """
                if (arguments[0].onchange) arguments[0].onchange();
                if (arguments[0].onblur) arguments[0].onblur();
            """
            from selenium.common.exceptions import WebDriverException
            try:
                elem.parent.execute_script(script, elem)
            except WebDriverException:
                pass
