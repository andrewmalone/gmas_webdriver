from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath

class SCR0232(Page):
    """
    SCR_0232 Subagreement List
    """
    locators = {
        "subagreement link": "css=a[href*='SubagreementEvent']",
        "subagreement row":  xpath.parent_row_of_event("SubagreementEvent")
    }
    
    
    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0232
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&SubagreementsLinkEvent=&segmentId={}&formName=SegmentHomeForm"
        return url.format(segment_id)
    

    @property
    def sub_count(self):
        """
        Count of subagreements in the list
        """
        return len(self.finds("subagreement link"))

    def goto_first_subagreement(self):
        """
        Clicks the first subagreement link on the page
        Goes to SCR_0450 or SCR_0233
        """
        return self.go("subagreement link")
    
    
    def sub(self, n):
        """
        Returns the nth subagreement row on the page
        //Subagreement_row
        """
        row = self.finds("subagreement row")[n - 1]
        return self.Subagreement_row(row, self)
    
    @property
    def sub_row(self):
        """
        List of all rows from the "Subagreement" table
        """
        return [self.Subagreement_row(row, self) for row in self.finds("subagreement row")]

    class Subagreement_row(Row):
        locators = {
            "link": "event=SubagreementEvent",
            "subrecipient": Row.cell(3),
            "Description": Row.cell(7),
            "id": Row.cell(11),
            "status": Row.cell(15),
            "pi": Row.cell(19),
            "dates": Row.cell(23),
            "dollars": Row.cell(27)
        }

        subrecipient = RText("subrecipient", "Subrecipient")
        description = RText("subrecipient", "Subrecipient")
        sub_id = RText("id", "Subagreement ID")
        status = RText("status", "Subagreement status")
        sub_pi = RText("pi", "Subrecipient PI")
        sub_dates = RText("dates", "Dates")
        sub_dollars = RText("dollars", "Dollars")

        def go(self):
            """
            Clicks the subagreement link
            Goes to SCR_0450 or SCR_0233
            """
            return self._go("link")
    
