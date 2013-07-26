from pages.Page import Page


class SCR0309(Page):
    locators = {
        "review completed": "name=ReviewCompletedEvent",
        "revise project": "name=CreateNewRevisionEvent"
    }

    def review_completed(self):
        return self.go("review completed")

    def revise_project(self):
        return self.go("revise project")
