from pages.Page import Page


class SCR0363(Page):
    """
    SCR_0363 View research team member (request)
    """
    locators = {
        "edit personnel": "name=EditPersonnelEvent",
        "delete": "DeleteResearchPersonnelEvent"
    }

    def edit_personnel(self):
        """
        Click <Edit personnel>
        Goes to SCR_0252
        """
        return self.go("edit personnel")

    def delete(self):
        """
        Click <Delete personnel>
        Goes to SCR_0398
        """
        return self.go("delete")
