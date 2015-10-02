from pages.Page import Page
from pages.elements import Row
from pages.elements import RText
import utilities.xpath as xpath
import utilities.url as url


class SCR0080(Page):
    """
    SCR_0080 Approval List
    """
    locators = {
        "approval link": "event=ApprovalListViewOrEditDetailEvent",
        "approval row": xpath.parent_row_of_event("ApprovalListViewOrEditDetailEvent")
    }
    
    _locators = {
        "approval link": "event=ApprovalListViewOrEditDetailEvent",
#         "approval row": "xpath=//span[contains(text(), 'Approval type')]/ancestor::table[1]//tr[not (@class ='bg3')][position()>1]"
        "approval row": "xpath=//tbody[@id='approvalsDatatable_data']/tr"
    }
    
#     @classmethod
#     def url(cls, segment_id):
#         """
#         Direct navigation to SCR_0015
#         """
#         url = "{{}}/gmas/dispatch?ref=%2Fproject%2Fincludes%2Fsegmenthome%2FSegmentHomeBody.jsp&segmentId={}&ApprovalListHomeEvent=&formName=SegmentHomeForm"
#          
#         return url.format(segment_id)

    @classmethod
    def url(cls, segment_id, request_id, user_id):
        """
        Direct navigation to SCR_0015
        """
        url = "{{}}/gmas/dispatch?ref=/request/includes/homedetails/ComponentsBodyPart2.jsp&segmentId={}&requestId={}&userId={}&formName=ApprovalsComponentListForm&ApprovalsComponentListViewListEvent=&segmentRevisionId=&submit"
        return url.format(segment_id, request_id, user_id)
   
    @property
    def approval_count(self):
        """
        Count of approvals in the list
        """
        return len(self.finds("approval link"))
# 
#     def goto_first_approval(self):
#         """
#         Click the first approval in the list
#         """
#         # TODO - document which pages here
#         return self.go("approval link")
# 
#     @property
#     def approvals(self):
#         """
#         List of all approval row objects
#         """
#         approvals = []
#         for row in self.finds("approval row"):
#             approvals.append(self.Approval_row(row, self))
#         return approvals


        


    def approval(self, n):
        """
        Returns the nth approval
        //Approval_row
        """
        row = self.finds("approval row")[n - 1]
        return self.Approval_row(row, self)
    
    @property
    def approval_row(self):
        """
        List of all rows from the "Approval" table
        """
        return [self.Approval_row(row, self) for row in self.finds("approval row")]

    class Approval_row(Row):
        locators = {
            "status": Row.cell(3),
            "approval type": Row.cell(7),
            "resp. party": Row.cell(11),
            "due date": Row.cell(15),
            "effective": Row.cell(19),
            "expires": Row.cell(23),
            "c": Row.cell(31)
        }
        
        _locators = {
            "status": Row.cell(2),
            "approval type": Row.cell(1),
            "resp. party": Row.cell(3),
            "due date": Row.cell(4),
            "effective": Row.cell(5),
            "expires": Row.cell(6),
            "c": Row.cell(7)
        }
        
        status = RText("status", "Status")
        approval_type = RText("approval type", "Approval type")
        resp_party = RText("resp. party", "Resp. party")
        due_date = RText("due date", "Due date")
        effective = RText("effective", "Effective")
        expires = RText("expires", "Expires")
        c = RText("c", "C")
        


#         @property
#         def type(self):
#             """
#             Approval type
#             """
#             return self.find("link").text
# 
#         @property
#         def status(self):
#             """
#             Approval status
#             """
#             return self.cell_text(3)
# 
#         @property
#         def huid(self):
#             """
#             HUID for the approval (if it is a person approval)
#             """
#             link = self.find("link").get_attribute("href")
#             return url.url_param(link, "HUID")
# 
#         @property
#         def approval_id(self):
#             """
#             Approval ID (from the url)
#             """
#             link = self.find("link").get_attribute("href")
#             return url.url_param(link, "approvalId")

#         def go(self):
#             """
#             Click the approval link
#             Goes to SCR_0081
#             """
#             return self._go("link")