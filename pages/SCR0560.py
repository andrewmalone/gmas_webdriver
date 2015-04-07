from pages.Page import Page
from pages.elements import Row
from pages.elements import RText


class SCR0560(Page):
    """
    SCR_0560 GL History for IDC Rate
    """
    locators = {
        "rate_row": "xpath=//td[contains(text(), 'Account indirect cost rates')]/ancestor::table[1]//tr[@class='bg0'][position()>1]",
        "history_row": "xpath=//td[contains(text(), 'History of general ledger feeds')]/ancestor::table[1]//tr[@class='bg0'][position()>1]"
    }
    _locators = {
        "rate_row": "css=[id$=currentRates_content] tbody tr",
        "history_row": "css=[id$=historicRates_content] tbody tr"
    }

    @classmethod
    def url(cls, segment_id, account_id):
        """
        Direct navigation to SCR_0560
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0187AccountDetail.jsp&ViewGLHistoryEvent=&accountId={}&segmentId={}&formName=AccountDetailForm"
        return url.format(account_id, segment_id)

    @property
    def rate_rows(self):
        """
        List of all rows from the "Account indirect cost rates" table
        """
        return [self.Rate_row(row, self) for row in self.finds("rate_row")]

    @property
    def history_rows(self):
        """
        List of all rows from the "History of general ledger feeds" table
        """
        return [self.History_row(row, self) for row in self.finds("history_row")]

    class Rate_row(Row):
        locators = {
            "rate": Row.cell(2),
            "date": Row.cell(6)
        }
        _locators = {
            "rate": Row.cell(1),
            "date": Row.cell(2)
        }
        rate = RText("rate", "IDC Rate")
        date = RText("date", "IDC Effective Date")

    class History_row(Row):
        locators = {
            "rate": Row.cell(2),
            "date": Row.cell(6),
            "gl_date": Row.cell(10)
        }
        _locators = {
            "rate": Row.cell(1),
            "date": Row.cell(2),
            "gl_date": Row.cell(3)
        }
        rate = RText("rate", "IDC Rate")
        date = RText("date", "IDC Effective Date")
        gl_date = RText("gl_date", "GL Effective Date")