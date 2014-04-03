from pages.Page import Page


class SCR0634(Page):
    """
    SCR_0634 Segment documents
    """
    locators = {
        "document": "event=DocumentActionViewEvent"
    }

    @property
    def document_count(self):
        """
        Number of documents shown
        """
        return len(self.finds("document"))
