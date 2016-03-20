from pages.Page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.elements import Row
import time


class cms(Page):
    locators = {
        "screen button": "css=[id$=screen-cd_display]",
        "screen input": "css=[id='cms-form:screen-cd'] input",
        "screen dropdown": "css=[data-item-label=REPLACE]",
        "IC header": "css=[id='cms-form'] h3:nth-of-type(1)",
        "IC content": "css=[id='cms-form'] h3:nth-of-type(1)+div",
        "IC rows": "css=[id='cms-form'] h3:nth-of-type(1)+div table",
        "IC add": "css=[id='cms-form'] h3:nth-of-type(1)+div button",
        "FC header": "css=[id='cms-form'] h3:nth-of-type(2)",
        "FC content": "css=[id='cms-form'] h3:nth-of-type(2)+div",
        "FC rows": "css=[id='cms-form'] h3:nth-of-type(2)+div table",
        "FC add": "css=[id='cms-form'] h3:nth-of-type(2)+div button",
        "GL header": "css=[id='cms-form'] h3:nth-of-type(3)",
        "GL content": "css=[id='cms-form'] h3:nth-of-type(3)+div",
        "GL rows": "css=[id='cms-form'] h3:nth-of-type(3)+div table table",
        "GL add": "css=[id='cms-form'] h3:nth-of-type(3)+div button",
        "dialog": "css=.ui-dialog[style*=block]",
        "content-id": "css=[id='cms-form:edit-content-id-']",
        "show source": "css=[id='cms-form:edit-content-'] div.ui-editor-button[title='Show Source']",
        "editor": "css=[id='cms-form:edit-content-'] textarea",
        "save": "id=cms-form:edit-dlg-save",
        "GL title": "css=input[id$=edit-title-]",
        "GL url": "css=input[id$=edit-url-]",
        "GL save": "css=button[id$=link-dlg-save]"
    }

    @classmethod
    def url(cls):
        """
        Direct navigation to the CMS page
        """
        url = "{}/gmas/admin/cms.xhtml"
        return url

    def enter_screen(self, scr):
        e = self.w.until(EC.element_to_be_clickable(self.get_locator("screen button")))
        e.click()
        e = self.w.until(EC.element_to_be_clickable(self.get_locator("screen input")))
        e.send_keys(scr)
        e = self.w.until(EC.element_to_be_clickable(self.get_locator("screen dropdown", scr)))
        e.click()
        self.w.until(EC.element_to_be_clickable(self.get_locator("IC header")))

    def edit_IC(self):
        e = self.find("IC content")
        if not e.is_displayed():
            self.find("IC header").click()
            self.w.until(lambda d: self.find("IC header").get_attribute("aria-expanded") == "true")
            time.sleep(.5)

    def edit_FC(self):
        e = self.find("FC content")
        if not e.is_displayed():
            self.find("FC header").click()
            self.w.until(lambda d: self.find("FC header").get_attribute("aria-expanded") == "true")
            time.sleep(.5)

    def edit_GL(self):
        e = self.find("GL content")
        if not e.is_displayed():
            self.find("GL header").click()
            self.w.until(lambda d: self.find("GL header").get_attribute("aria-expanded") == "true")
            time.sleep(.5)

    def add_IC(self, id, content):
        self.find("IC add").click()
        self.w.until(EC.element_to_be_clickable(self.get_locator("dialog")))
        self.add_dynamic(id, content)

    def add_FC(self, id, content):
        self.find("FC add").click()
        self.w.until(EC.element_to_be_clickable(self.get_locator("dialog")))
        self.add_dynamic(id, content)

    def add_dynamic(self, id, content):
        self.find("content-id").send_keys(id)
        self.find("show source").click()
        self.find("editor").send_keys(content)
        self.find("save").click()
        self.w.until(EC.invisibility_of_element_located(self.get_locator("save")))

    def add_GL(self, id, content):
        self.find("GL add").click()
        self.w.until(EC.element_to_be_clickable(self.get_locator("dialog")))
        self.find("GL title").send_keys(content)
        self.find("GL url").send_keys(id)
        self.find("GL save").click()
        self.w.until(EC.invisibility_of_element_located(self.get_locator("GL save")))

    @property
    def IC_rows(self):
        return [self.Content_row(row, self) for row in self.finds("IC rows")]

    @property
    def GL_rows(self):
        return [self.Content_row(row, self) for row in self.finds("GL rows")]

    @property
    def FC_rows(self):
        return [self.Content_row(row, self) for row in self.finds("FC rows")]

    class Content_row(Row):
        locators = {
            "delete": "css=tr:nth-of-type(1) td a:nth-of-type(2)",
            "delete link": "css=td:nth-child(3) a"
        }

        def delete(self):
            try:
                self.find("delete").click()
            except:
                e = self.find("delete link")
                ActionChains(self.page.driver).double_click(e).perform()
