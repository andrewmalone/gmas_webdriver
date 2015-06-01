from pages.Page import Page
from pages.elements import Row, RText
import utilities.xpath as xpath


class SCR0425(Page):
    """
    SCR_0425 Segment revision list
    """
    locators = {
        "revision row": xpath.parent_row_of_event("ListOfRevisionsAppliedRevisionDetailEvent"),
        "open comments": "xpath=//a[contains(text(),'open all comments')]",
        "comments": "xpath=//*[contains(normalize-space(text()), 'Revision Id')]/ancestor::tr[1]/following-sibling::tr[1]",
        "revision id": "xpath=//*[contains(normalize-space(text()), 'Revision Id')]"
    }

    _locators = {
        "revision row": xpath.parent_row_of_event("ListOfRevisionsAppliedRevisionDetailEvent"),
        "open comments": "css=a.open-all",
        "comments": "id=actionMemosDatatable:num:commentValue"
#          
    }
    @classmethod
    def url(cls, segment_id):
 
        """
        Direct navigation to SCR_0453
        """
        url = "{{}}/gmas/dispatch?ref=/project/includes/segmenthome/RightColumn.jsp&segmentId={}&formName=SegmentHomeForm&SegmentHomeRevisionListEvent=&submit"
        return url.format(segment_id)
    
    
    @property
    def revision_count(self):
        """
        Number of revisions
        """
        return len(self.finds("revision row"))
    
    
    def open_comments(self):
         """
         Click the open all comments
         opens all the comments
         """
#          print self.find("open comments")
#          self.find("open comments").text
         self.find("open comments").click()
    
    @property
    def comments(self):
        """
        View the comments
        """
        revision_id = self.revision_id
        row = self.page.find_element("comments")
        return row.text
    
#     @property
#     def revision_id(self):
#         """
#         View revision id
#         """
#         revision_id = self.page.find_element("revision id")
#         return revision_id
    
        
    def revision(self, n):
        """
        Returns the nth revision row
        //Revision
        """
        row = self.finds("revision row")[n - 1]
        return self.Revision(row, self)
    
    @property
    def revisions(self):
        """
        Returns the nth request in the list
        revision row
        """
        return [self.Revision(row, self) for row in self.finds("revision row")]
    

    class Revision(Row):
        locators = {
            "link": "event=ListOfRevisionsAppliedRevisionDetailEvent",
            "date initiated": Row.cell(2),
            "date committed": Row.cell(6),
            "revision id": Row.cell(10),  
            "type": Row.cell(14),
            "status": Row.cell(18),
            "created by": Row.cell(22),
            "committed by": Row.cell(26),
               
        }
         
        _locators = {
            "link": "event=ListOfRevisionsAppliedRevisionDetailEvent",
            "date initiated": Row.cell(1),
            "date committed": Row.cell(2),
#             "revision id": Row.cell(),  
            "type": Row.cell(3),
            "status": Row.cell(4),
            "created by": Row.cell(5),
            "committed by": Row.cell(6),
             
        }

        date_initiated = RText("date initiated", "Date initiated")
        date_committed = RText("date committed", "Date committed")
#         revision_id = RText("revision id", "Revision id")
        type = RText("type", "Type")
        status = RText("status", "Status")
        created_by = RText("created by", "Created by")
        committed_by = RText("committed by", "Committed by")
        
        
        
        def go(self):
                """
                Click the revision link
                Goes to SCR_0426
                """
                return self._go("link")
        
        @property
        def comment(self):
            from selenium.common.exceptions import NoSuchElementException
            if self.page.mode == "old":
                try:
                    self.driver.find_element_by_css_selector("[id='minusIconId']")
                    has_comment = True
                except NoSuchElementException:
                    has_comment = False
                revision_id = self.find("revision id").text
                locator = "xpath=//*[contains(normalize-space(text()), '{}')]/ancestor::tr[1]/following-sibling::tr[1]".format(revision_id)
            if self.page.mode == "convert":
                try:
                    self.driver.find_element_by_css_selector("div.ui-row-toggler")
                    has_comment = True
                except NoSuchElementException:
                    has_comment = False
                num = self.driver.get_attribute("data-ri")
                locator = "id=actionMemosDatatable:{}:commentValue".format(num)
            # print has_comment, locator
            if has_comment:
                comment = self.page.find_element(locator)
                return comment.text
            else:
                return None
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
