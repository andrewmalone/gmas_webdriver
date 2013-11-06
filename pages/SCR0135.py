from pages.Page import Page


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
        "checkin": "name=DocumentActionCheckInEvent"
    }

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