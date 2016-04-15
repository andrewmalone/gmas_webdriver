from pages.Page import Page
from pages.elements import Row
from pages.elements import RText, Radio, Select, Text, Checkbox
import utilities.xpath as xpath


class SCR0135(Page):
    """ SCR_0135 Document Detail """
    locators = {
        "unlock": "name=DocumentUnlockEvent",
        "unlock version": "name=DocumentActionUnlockVersionEvent",
        "download": "css=a[href*='DocumentActionViewEvent'] img",
        "delete": "name=DocumentActionDeleteEvent",
        "rename": "name=DocumentActionRenameEvent",
        "edit_desc": "name=DocumentActionEditDescriptionEvent",
        "checkout": "name=DocumentActionCheckOutEvent",
        "checkin": "name=DocumentActionCheckInEvent",
        "description": "xpath=//td[contains(normalize-space(text()), 'Description')]//following-sibling::td[2]",
        "version": "xpath=//td[contains(normalize-space(text()), 'Version')]//following-sibling::td[2]",
        "type": "xpath=//td[contains(normalize-space(text()), 'Type')]//following-sibling::td[2]",
        "size": "xpath=//td[contains(normalize-space(text()), 'Size')]//following-sibling::td[2]",
        "status": "xpath=//td[contains(normalize-space(text()), 'Status')]//following-sibling::td[2]",
        "modified on": "xpath=//td[contains(normalize-space(text()), 'Modified on')]//following-sibling::td[2]",
        "modified by": "xpath=//td[contains(normalize-space(text()), 'Modified by')]//following-sibling::td[2]" ,
        "checked in": "xpath=//td[contains(normalize-space(text()), 'Checked in on')]//following-sibling::td[2]",
        "checked by": "xpath=//td[contains(normalize-space(text()), 'Checked in by')]//following-sibling::td[2]",
        "segment repository": "xpath=//a[contains(text(),'Segment repository')]"
    }
    
    @classmethod
    def url(cls, segment_id,):
        """
        Direct navigation to segmenthome
        """
        url = "{{}}/gmas/dispatch?ref=%2Fproject%2FCOM0500ProjectSnapshot.jsp&formName=COM0500ProjectSnapshotForm&segmentId={}&ProjectSnapShotSegmentHomeEvent=&submitTime=1460395801417"
        return url.format(segment_id,)
    
    desscription = RText("description", "Description")
    check_in = RText("checked in", "Checked in on")
    check_by =  RText("checked by", "Ckecked in by") 
#     version =  RText("version", "Version") 
#     type =  RText("type", "Type") 
    size =  RText("size", "Size(bytes)")
#     status =  RText("status", "Status") 
#     modified_on =  RText("modified on", "Modified on")
#     modified_by =  RText("modified by", "Modified by") 

    def unlock(self):
        """
        Click the <unlock> button
        """
        return self.go("unlock")

    def unlock_version(self):
        """
        Click the <Unlock version> button
        """
        return self.go("unlock version")

    def delete(self):
        """
        Click the <Delete> button
        Goes to SCR_0136
        """
        return self.go("delete")

    def rename(self):
        """
        Click the <Rename> button
        Goes to SCR_0137
        """
        return self.go("rename")

    def edit_desc(self):
        """
        Click the <Edit description> button
        Goes to SCR_0137
        """
        return self.go("edit_desc")

    def checkout(self):
        """
        Click the <Check out to edit> button
        """
        return self.go("checkout")

    def checkin(self):
        """
        Click the <Check in after edit> button
        Goes to SCR_0138
        """
        return self.go("checkin")
    
    def segment_repository(self):
        """
        Click the <segment repository> link in the breadcrumb
        Goes back to SCR_0433
        """
        return self.go("segment repository")