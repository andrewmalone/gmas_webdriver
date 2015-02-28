# @todo - refactor using the Row element class
from pages.Page import Page, GMWebElement
from pages.lookups import Lookup_person
from pages.elements import Text, Select


class SCR0649(Page):
    """
    SCR_0649 Edit research team
    """
    locators = {
        "row": "css=#dataRow:not([style*='display: none'])",
        "add input": "name=personName",
        "cancel": "EditResearchTeamCancelEvent",
        "ok": "EditResearchTeamOkEvent"
    }

    add_member_text = Text("add input", "Text box for adding a new person")
    add_member = Lookup_person(add_member_text, "personLookupImage", "Lookup for adding a research team member")

    def count_rows(self):
        """
        test1
        """
        return len(self.finds("row"))

    def row(self, rownum):
        """
        test2
        """
        return self.Row(self.finds("row")[rownum - 1], self)

    def cancel(self):
        """
        Click <Cancel>
        Goes to SCR_0015
        """
        return self.go("cancel")

    def ok(self):
        """
        Click <Ok>
        Goes to SCR_0015
        """
        return self.go("ok")

    class Row(GMWebElement):
        """
        test3
        """
        locators = {
            "name": "id=personName",
            "role": "css=#roleText select",
            "role text": "css=#roleText",
            "other role": "css=input[name$=otherRoleDescription]",
            "key": "css=select[name$=isKeyPerson]",
            "phs": "css=select[name$=isMemberPHSInvestigator]",
            "hs": "css=select[name$=isMemberInvolvedWithHumanSubjects]",
            "cal": "id=calculatedEffortId",
            "acad": "id=academicEffortId",
            "sum": "id=summerEffortId",
            "eff_date": "css=input[name$=committedEffortEffectivedate]",
            "sc": "css=[name$=sponsorCommitmentFlag]",
            # I think this locator is iffy - very structure dependent
            "current": "css=td > #datatable td"
        }

        role = Select("role")
        other_role = Text("other role")
        key = Select("key")
        phs = Select("phs")
        hs = Select("hs")
        cal = Text("cal")
        acad = Text("acad")
        summer = Text("sum")
        effective_date = Text("eff_date")
        sponsor_commitment = Select("sc")

        def __init__(self, row, page):
            self.driver = row
            self.name = self.find("name").text
            self.current_effort = self.find("current").text

        def is_phs_editable(self):
            return True if self.find("phs").is_displayed() else False

        def is_key_editable(self):
            return True if self.find("key").is_displayed() else False

        def is_role_editable(self):
            return True if self.find("role").is_displayed() else False

        def is_sponsor_commitment_editable(self):
            return True if self.find("sc").is_displayed() else False

        def is_commitment_editable(self):
            from selenium.common.exceptions import NoSuchElementException
            try:
                self.find("cal")
            except NoSuchElementException:
                return False
            return True

        # This is here to ovveride the __get__ method of the select if the select
        # is not actually displayed. I'm sure there is a better way to do it, but
        # this works for now.
        def __getattribute__(self, key):
            # special case for sponsor commitment if it is not a select
            if key == "sponsor_commitment" and self.find("sc").tag_name == "input":
                return self.find("sc").find_element_by_xpath("..").text

            v = object.__getattribute__(self, key)

            # override the return value if the select is not displayed
            if key in ["role", "key", "phs"] and v.is_displayed() is False:
                return self.find(key).find_element_by_xpath("..").text

            if hasattr(v, '__get__'):
                    #print "inside (%s)" % key
                    return v.__get__(None, self)
            return v

