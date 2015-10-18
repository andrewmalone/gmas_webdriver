from pages.Page import Page
from pages.elements import Text
from pages.lookups import Lookup_person


class SCR0295(Page):
    """
    SCR_0295 Edit financial report
    """
    locators = {
        "cancel": "EditScheduledFinancialReportCancelEvent",
        "ok": "EditScheduledFinancialReportOkEvent",
        "invoice_number": "invoiceNumber",
        "invoice_date": "invoiceDate",
        "invoice_amount": "invoiceAmount",
        "date_started": "preparationStartDate",
        "date_completed": "reportCompletionDate",
        "completed_by": "submittedBy",
        "comments": "financialScheduledReportComment"
    }

    completed_by_text = Text("completed_by", "Completed by input box")
    completed_by = Lookup_person(completed_by_text, "submittedByImage", "Lookup for person completing the report")
    invoice_number = Text("invoice_number")
    invoice_date = Text("invoice_date")
    invoice_amount = Text("invoice_amount")
    date_started = Text("date_started")
    date_completed = Text("date_completed")
    comments = Text("comments")

    @classmethod
    def url(cls, segment_id, report_id):
        """
        Direct navigation to SCR_0295
        """
        url = "{{}}/gmas/dispatch?EditScheduledFinancialReportEvent=&ref=%2Fscheduledreport%2FSCR0297ScheduledFinancialReport.jsp&formName=ScheduledFinancialReportForm&segmentId={}&scheduledReportId={}"
        return url.format(segment_id, report_id)

    def cancel(self):
        """
        Click <Cancel>
        Goes to SCR_0297
        """
        return self.go("cancel")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0297, SCR_0150 (or final figure)
        """
        return self.go("ok")
