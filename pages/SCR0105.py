from pages.Page import Page

#TODO Confirm deleting revision always returns to segment home
#TODO move delete confirm to own page object

locators = {
    "commit changes" : "name=CommitSegmentRevisionEvent",
    "edit allocation" : "name=EditAllocationOfAwardedFundsEvent",
    "edit sponsors" : "name=EditSponsorsInformationEvent",
    "edit accounts" : "name=EditAccountsEvent",
    "edit id info" : "name=EditAwardIdentifyingInformationEvent",
    "delete revision" : "name=DeleteThisRevisionEvent",
    "revision id" : "name=segmentRevisionId"
}

class SCR0105(Page):        
    def nav_to(self,segment_id,revision_id):
        url = "https://%s.harvard.edu/gmas/dispatch?segmentId=%s&SegmentHomeEditRevisionEvent=&formName=SegmentHomeForm&segmentRevisionId=%s" %(self.env,segment_id,revision_id)
        self.driver.get(url)
        return SCR0105(self.driver)

    def edit_allocation(self):
        self.find_element(locators["edit allocation"]).click()
        self.w.until(lambda d: d.find_element_by_css_selector("input[name=ref][value*=SCR0427]"))
        from pages.SCR0427 import SCR0427
        return SCR0427(self.driver)
        
    def edit_sponsors(self):
        self.find_element(locators["edit sponsors"]).click()
        from pages.SCR0324 import SCR0324
        return SCR0324(self.driver)
    
    def edit_id_info(self):
        self.find_element(locators["edit id info"]).click()
        from pages.SCR0328 import SCR0328
        return SCR0328(self.driver)
    
    def delete_revision(self):
        self.find_element(locators["delete revision"]).click()
        self.find_element("name=OkDeleteProjectRevisionEvent").click()
        from pages.SCR0104b import SCR0104b
        return SCR0104b(self.driver)
        
    def delete_revision_confirm(self):
        pass
    
    def edit_account(self):
        self.find_element(locators["edit accounts"]).click()
        from pages.SCR0196 import SCR0196
        return SCR0196(self.driver)
    
    def commit_changes(self):
        self.find_element(locators["commit changes"]).click()
        self.w.until(lambda d: len(d.find_elements_by_css_selector("input[name=eventSubmittedByWaitScreen]")) == 0)
        return self.load_page()
    
    def get_revision_id(self):
        return self.find_element(locators["revision id"]).get_attribute("value")
