from pages.Page import Page


class SCR0134a(Page):
    """
    SCR_01134a Organization Profile
    """
    locators = {
        "documents": "event=RepositoryLinkEvent",
        "edit id info": "ViewEditInternalOrganizationDetailsEvent",
        "edit chart": "event=ViewEditChartOfAccountsAttributeEvent",
        "edit sig": "event=InternalOrganizationEditOrgSignatureRulesEvent"
    }

    def goto_documents(self):
        """
        Clicks the "Documents" link
        Goes to SCR_0433
        """
        return self.go("documents")

    def edit_identifying_info(self):
        """
        Clicks the <edit> button for Indentifying information
        Goes to SCR_0217a
        """
        return self.go("edit id info")

    def edit_chart_ranges(self):
        """
        Clicks the <edit> button for Chart of account value ranges
        Goes to SCR_0524
        """
        return self.go("edit chart")

    def edit_signatures(self):
        """
        Clicks the <edit> button for signatures
        Goes to SCR_0510a, SCR_0510b, or SCR_0510c
        """
        return self.go("edit sig")
