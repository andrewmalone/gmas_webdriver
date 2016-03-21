from pages.Page import Page


class SCR0634(Page):
    """
    SCR_0634 Segment documents
    """
    locators = {
        "document": "event=DocumentActionViewEvent",
        "email": "event=EmailLinkEvent"
    }

    @classmethod
    def url(cls, segment_id):
        """
        Direct navigation to SCR_0634
        """
        url = "{{}}/gmas/dispatch?ref=/project/includes/segmenthome/RightColumn.jsp&formName=SegmentHomeForm&segmentId={}&SegmentDocumentsLinkEvent="
        return url.format(segment_id)

    @property
    def document_count(self):
        """
        Number of documents shown
        """
        return len(self.finds("document"))

    @property
    def email_count(self):
        """
        Number of emails shown
        """
        return len(self.finds("email"))
