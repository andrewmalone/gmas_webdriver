from pages.Page import Page
from pages.lookups import Lookup_person
from pages.elements import Text, RText, Select, Row


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

    @property
    def person_count(self):
        """
        Number of people in the research team list
        """
        return len(self.finds("row"))

    def person(self, n):
        """
        Returns row for the nth person on the screen
        //Person_Row
        """
        return self.Person_Row(self.finds("row")[n - 1], self)

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

    class Person_Row(Row):
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
            "delete": "id=delIcon",
            # I think this locator is iffy - very structure dependent
            "current": "css=td > #datatable td"
        }

        name = RText("name", "Team member name")
        current_effort = RText("current", "Current effort")
        role = Select("role", "Role")
        other_role = Text("other role", "Other role edit box")
        key = Select("key", "Key flag")
        phs = Select("phs", "PHS Investigator flag")
        hs = Select("hs", "Human subjects flag")
        cal = Text("cal", "Calendar effort")
        acad = Text("acad", "Academic effort")
        summer = Text("sum", "Summer effort")
        effective_date = Text("eff_date", "Effective date")
        sponsor_commitment = Select("sc", "Sponsor commitment")

        def is_phs_editable(self):
            """
            returns True/False if the investigator flag is editable
            """
            return True if self.find("phs").is_displayed() else False

        def is_key_editable(self):
            """
            returns True/False if the key flag is editable
            """
            return True if self.find("key").is_displayed() else False

        def is_role_editable(self):
            """
            returns True/False if the role is editable
            """
            return True if self.find("role").is_displayed() else False

        def is_sponsor_commitment_editable(self):
            """
            returns True/False if the sponsor commitment flag is editable
            """
            return True if self.find("sc").is_displayed() else False

        def is_commitment_editable(self):
            """
            returns True/False if the commitment is editable
            """
            from selenium.common.exceptions import NoSuchElementException
            try:
                self.find("cal")
            except NoSuchElementException:
                return False
            return True

        def delete(self):
            """
            Delete the person
            """
            self.find("delete").click()

        # This is here to ovveride the __get__ method of the select if the select
        # is not actually displayed. I'm sure there is a better way to do it, but
        # this works for now.
        def __getattribute__(self, key):
            # print key
            # special case for sponsor commitment if it is not a select
            if key == "sponsor_commitment" and self.find("sc").tag_name == "input":
                return self.find("sc").find_element_by_xpath("..").text

            v = object.__getattribute__(self, key)

            # override the return value if the select is not displayed
            if key in ["role", "key", "phs"] and v.is_displayed() is False:
                # print "override"
                return self.find(key).find_element_by_xpath("..").text

            if hasattr(v, '__get__'):
                    # print "inside (%s)" % key
                    return v.__get__(None, self)
            return v
