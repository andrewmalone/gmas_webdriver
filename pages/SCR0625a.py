from pages.Page import Page
from pages.elements import Text


class SCR0625a(Page):
    """
    SCR_0625a Re-enable subactivity
    """
    locators = {
        "ok": "ReenableSubactivityConfirmationOkEvent",
        "date": "glDateReenable"
    }

    date = Text("date", "Re-enable date")

    @classmethod
    def url(cls, segment_id, account_id, subactivity_id, fund):
        """
        Return a direct url for SCR_0625a
        Example query:
        ````
        select
          ag.segment_id,
          a.account_id,
          sub.subactivity_id,
          a.fund
        from
          rf_subactivities sub
          join accounts a on a.subactivity_id = sub.subactivity_id
          join rf_gl_feed_statuses gl on sub.gl_feed_status_id = gl.gl_feed_status_id
          join rf_coa_segment_statuses coa on sub.coa_segment_status_id = coa.coa_segment_status_id
          join account_groups ag on a.account_group_id = ag.account_group_id
          join rf_funds fund on a.fund = fund.fund
          join rf_coa_segment_statuses f_coa on fund.COA_SEGMENT_STATUS_ID = f_coa.COA_SEGMENT_STATUS_ID
        where
          f_coa.description = 'Enabled'
          and coa.description = 'Disabled'
          and gl.description = 'Reconciled'
        ````
        """
        url = "{{}}/gmas/dispatch?ref=%2Faccount%2FSCR0187AccountDetail.jsp&accountId={account}&segmentId={segment}&formName=AccountDetailForm&subactivityId={subactivity}&fund={fund}&ViewSubactivityDetailsEvent="
        return url.format(segment=segment_id, account=account_id, fund=fund, subactivity=subactivity_id)

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0187
        """
        return self.go("ok")
