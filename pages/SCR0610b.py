from pages.Page import Page


class SCR0610b(Page):
    """
    SCR_0610b Grants.gov attachments (RGS/Req Home)
    """
    locators = {
        "next": "name=GrantsGovAttachmentsNextEvent",
        "ok": "name=GrantsGovAttachmentsOkEvent",
        "locate all": "css=a[href*='GrantsGovAttachmentsLocateEvent']",
        "locate form": "css=a[href*='GrantsGovAttachmentsLocateEvent'][href*='FORM'][href$='ATTACHMENT']"
    }

    def locate_buttons(self, form_name, attachment_name):
        """
        returns a list of <locate> buttons matching the form/attachment name combo
        form_name is as displayed in the component on SCR_0610b, attachment_name is also as displayed on the screen. For key person attachments, attachment_name should not include the person name
        for example: locate_buttons("Research & Related Budget","Budget Justification") will return a list of <locate> buttons for that attachment.
        """
        # returns a collection! (is this good?)
        import urllib
        form_name = urllib.quote_plus(form_name)
        attachment_name = urllib.quote_plus(attachment_name)
        locator = self.locators["locate form"].replace("FORM", form_name).replace("ATTACHMENT", attachment_name)
        return self.find_elements(locator)

    def locate(self, locate_button):
        """
        Click a locate button to go to SCR_0611
        locate_button needs to be a selenium webelement. This is most likely to be used in conjuction with the locate_buttons() method - for example: 
        * locate(locate_buttons("Research & Related Budget","Budget Justification")[0]) will click the budget justification <locate> button
        * locate(locate_buttons("Research & Related Key Person Expanded","Biographical Sketch")[2]) will click the third biosketch <Locate> button
        """
        locate_button.click()
        return self.load_page()

    def ok(self):
        """
        Click <Next> or <Ok>
        Goes to SCR_0332 or SCR_0115
        """
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.find("next").click()
        except NoSuchElementException:
            self.find("ok").click()
        return self.load_page()
