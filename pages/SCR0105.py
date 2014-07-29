from pages.Page import Page


class SCR0105(Page):
    """
    SCR_0105 Segment Revision home
    """
    locators = {
        "commit changes": "name=CommitSegmentRevisionEvent",
        "edit allocation": "name=EditAllocationOfAwardedFundsEvent",
        "edit sponsors": "name=EditSponsorsInformationEvent",
        "edit accounts": "name=EditAccountsEvent",
        "edit id info": "name=EditAwardIdentifyingInformationEvent",
        "edit dates": "EditAwardedDatesEvent",
        "delete revision": "name=DeleteThisRevisionEvent",
        "revision id": "name=segmentRevisionId",
        "edit all": "name=EditAllEvent"
    }

    def nav_to(self, segment_id, revision_id):
        """
        Shortcut method to navigate to an open revision
        """
        url = "https://%s.harvard.edu/gmas/dispatch?segmentId=%s&SegmentHomeEditRevisionEvent=&formName=SegmentHomeForm&segmentRevisionId=%s" % (self.env, segment_id, revision_id)
        self.driver.get(url)
        return SCR0105(self.driver)

    def edit_allocation(self):
        """
        Click <edit> for account allocations
        Goes to SCR_0427
        """
        return self.go("edit allocation")

    def edit_sponsors(self):
        """
        Click <edit> for sponsors
        Goes to SCR_0324
        """
        return self.go("edit sponsors")

    def edit_id_info(self):
        """
        Click <edit> for Award identifying information
        Goes to SCR_0328
        """
        return self.go("edit id info")

    def edit_accounts(self):
        """
        Click <edit> for accounts
        Goes to SCR_0196
        """
        return self.go("edit accounts")

    def edit_dates(self):
        """
        Click <edit> for awarded edit_dates
        Goes to SCR_0359
        """
        return self.go("edit dates")

    def commit_changes(self):
        """
        Click <Commit changes>
        Goes to SCR_0100 (through the wait screen)
        """
        return self.go("commit changes")

    def edit_all(self):
        """
        Click <Edit all>
        Goes to SCR_0328
        """
        return self.go("edit all")
