import gmas_webdriver
from gmas_webdriver.scenarios import data
from common import research_team_record, standard_team


class COI_Test:
    @classmethod
    def setup_class(self):
        self.should_teardown = True
        self.p = gmas_webdriver.init("Chrome", "gint", True)

    @classmethod
    def teardown_class(self):
        # self.should_teardown = False
        if self.should_teardown:
            self.p.quit()

    def setup_method(self, method):
        # print "setup"
        pi = data.random_huid_with_name()
        self.pi_huid = pi[0]
        self.pi_name = pi[1]
        self.team = [{
            "huid": self.pi_huid,
            "name": self.pi_name,
            "role": "Principal Investigator",
            "key": "true",
            "investigator": "true",
            "hs": "false",
            "university": pi[2]
        }]
        self.deleted_approvals = {}
        self.approvals = {}
        self.approval_context = None

    def teardown_method(self, method):
        # return to GMAS home
        if self.should_teardown:
            self.p = self.p.global_header.goto_home()
        # pass

    def add_person_to_team(self, key, investigator, university=None):
        # only adds in test's "team" object - not in GMAS
        self.team.append(research_team_record(key, investigator, university))

    def add_standard_team(self):
        for person in standard_team:
            self.add_person_to_team(**person)

    def submit_oar_create(self):
        from gmas_webdriver.interfaces.oar import submit_oar_create
        submit_oar_create(self.p)

    def get_approvals(self):
        """
        assume on request or segment home
        """
        approvals = {}
        p = self.p.goto_approvals()
        # get the approval context - request or segment
        request_id = p.get_id("request")
        if request_id is not None:
            self.approval_context = ("request", self.request_type, request_id)
        else:
            self.approval_context = ("segment")
        for approval in p.approvals:
            if approval.type in ["OAR Conflict of Interest", "Conflict of Interest"]:
                huid = approval.huid
                new_approval = {
                    "id": approval.approval_id,
                    "type": "OAR" if approval.type == "OAR Conflict of Interest" else "FCOI",
                    "status": approval.status
                }
                if huid in approvals:
                    approvals[huid].append(new_approval)
                else:
                    approvals[huid] = [new_approval]
        self.p = p.back()
        self.approvals = approvals

    def flag_deleted_approval(self, huid, db_delete):
        if huid in self.approvals:
            print "delete approval for {}".format(huid)
            # check the existing approval status to see if the approval should be in the delete queue
            for approval in self.approvals[huid]:
                if approval["type"] == "FCOI":
                    approval["queue"] = False
                if approval["type"] == "OAR":
                    if approval["status"] in ["Pending", "Withdrawn"]:
                        approval["queue"] = False
                    else:
                        approval["queue"] = True
                approval["db_delete"] = db_delete
                approval["huid"] = huid
                self.deleted_approvals[approval["id"]] = approval

    def print_person(self, person):
        print self.get_format_string().format(**person)

    def print_person_header(self):
        print self.get_format_string().format(huid="HUID", name="NAME", role="ROLE", key="KEY", investigator="INV", university="UNV")

    def print_team(self):
        approvals = self.approvals
        keys = approvals.keys()
        self.print_person_header()
        for person in self.team:
            self.print_person(person)
            huid = person["huid"]
            if huid in approvals:
                for approval in approvals[huid]:
                    print "  {} Approval {}: {}".format(approval["type"], approval["id"], approval["status"])
                keys.remove(huid)
        if len(keys) > 0:
            print "Some left over!"

    def get_format_string(self):
        # keys are hardcoded to get them in the right order
        keys = [
            "huid",
            "name",
            "role",
            "key",
            "investigator",
            "university"
        ]

        format_string = ""

        for key in keys:
            field_length = max([len(f[key]) for f in self.team]) + 3
            format_string += "{{{0}: <{1}}}".format(key, field_length)

        return format_string

    def assert_approvals(self, output=True):
        self.get_approvals()
        if output:
            self.print_team()

        # check the approvals for people currently on the team
        approvals = self.approvals
        keys = approvals.keys()
        for person in self.team:
            oar_count = 0
            fcoi_count = 0
            huid = person["huid"]
            if huid in approvals:
                for approval in approvals[huid]:
                    if approval["type"] == "OAR":
                        if approval["id"] in self.deleted_approvals:
                            assert self.deleted_approvals[approval["id"]]["db_delete"] is False
                        else:
                            oar_count += 1
                    if approval["type"] == "FCOI":
                        if approval["id"] in self.deleted_approvals:
                            assert self.deleted_approvals[approval["id"]]["db_delete"] is False
                        else:
                            fcoi_count += 1
                keys.remove(huid)

            self.print_person(person)
            oar_assert = (1 if (person["investigator"] == "true" and self.tub == "520") else 0)
            if self.approval_context[0] == "request" and self.approval_context[1] == "continuation":
                # for continuations
                if person["source"] != self.approval_context:
                    oar_assert = 0

            assert oar_count == oar_assert
            assert fcoi_count == (1 if (self.tub != "520" and (person["investigator"] == "true" or person["university"] == "1")) else 0)

        # check on any leftover approvals
        for huid in keys:
            for approval in approvals[huid]:
                # check that this should be here...
                print self.deleted_approvals.keys()
                assert approval["id"] in self.deleted_approvals
                assert self.deleted_approvals[approval["id"]]["db_delete"] is False
                # print self.deleted_approvals[approval["id"]]

        self.assert_removal_queue()

    def assert_removal_queue(self):
        local_removals = [approval_id for approval_id in self.deleted_approvals if self.deleted_approvals[approval_id]["queue"] is True]
        from gmas_webdriver.interfaces.oar import removal_queue_for_segment
        database_removals = removal_queue_for_segment(self.segment_id, self.p)
        print local_removals, database_removals
        for removal in local_removals:
            assert removal in database_removals
            database_removals.remove(removal)
        assert len(database_removals) == 0
