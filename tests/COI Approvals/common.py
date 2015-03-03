# import unittest
import gmas_webdriver
from gmas_webdriver.scenarios import data
from gmas_webdriver.scripts.request import rgs, samples, initiate, submit
from gmas_webdriver.scripts.notice import log_notice
from gmas_webdriver.scripts.research_team import confirm_team, fill_commitments

standard_team = [
        {
            "key": "true",
            "investigator": "true",
            "university": "1"
        },
        {
            "key": "true",
            "investigator": "true",
            "university": "0"
        },
        {
            "key": "true",
            "investigator": "false",
            "university": "1"
        },
        {
            "key": "true",
            "investigator": "false",
            "university": "0"
        },
        {
            "key": "false",
            "investigator": "true",
            "university": "1"
        },
        {
            "key": "false",
            "investigator": "true",
            "university": "0"
        },
        {
            "key": "false",
            "investigator": "false",
            "university": "1"
        },
        {
            "key": "false",
            "investigator": "false",
            "university": "0"
        }
    ]


def req_with_team(pi, team, title, org="31240", sponsor="nih"):
    """
    Returns an rgs object with the specified research team
    pi: HUID string
    team: research team data object
    """
    req = samples.minimal
    req["pi"] = pi
    req["org"] = org
    req["sponsor"] = sponsor
    req["research team"] = team
    req["title"] = samples.add_ts(title)
    return req


def research_team_record(key, investigator, university=None):
    """
    Returns a research team dictionary for use in an rgs data object
    key and investigator should be "true" or "false"
    """
    person = data.random_huid_with_name(university=university)

    team_member = {
        "huid": person[0],
        "name": person[1],
        "role": data.random_research_team_role(),
        "hs": "false",
        "key": key,
        "investigator": investigator,
        "university": person[2]
    }
    return team_member


def map_value(value):
    if value == "true":
        return "Yes"
    elif value == "false":
        return "No"
    return value


class COI_Test:
    @classmethod
    def setup_class(self):
        self.should_teardown = False
        self.p = gmas_webdriver.init("Chrome", "gdev", "true")
        self.approvals = {}

    @classmethod
    def teardown_class(self):
        if self.should_teardown:
            self.p.quit()
        # pass

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

    def add_person_after_rgs(self, key, investigator, university=None):
        p = self.p
        # add in GMAS
        person = research_team_record(key, investigator, university)
        p = p.goto_research_team().add_team_member()
        p.name = person["huid"]
        p.human_subjects = person["hs"]
        p.role = person["role"]
        p.set_key(person["key"])
        p.phs = person["investigator"]
        p.set_effort("0")
        p.appt = "12"
        p = p.ok().back()
        self.p = p
        self.team.append(person)

    def add_standard_team_after_rgs(self):
        for person in standard_team:
            self.add_person_after_rgs(**person)

    def change_flag_for_request_person(self, index):
        """
        Change the investigator flag for a person on the team (request!)
        """
        current_flag = self.team[index]["investigator"]
        new_flag = "true" if current_flag == "false" else "false"
        p = self.p.goto_research_team().goto_role(index + 1)
        p = p.edit_personnel()
        p.phs = new_flag
        p.appt = "12"
        self.team[index]["investigator"] = new_flag
        self.flag_deleted_approval(self.team[index]["huid"], True)
        p = p.ok().back(2)
        self.p = p

    def change_all_request_flags(self):
        """
        Flips the investigator flag for all people on the research team (not PI)
        """
        for i in range(1, len(self.team)):
            self.change_flag_for_request_person(i)

    def flag_deleted_approval(self, huid, db_delete):
        if huid in self.approvals:
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

    def delete_all_request_people(self):
        """
        Removes everyone from the request research team except the PI
        """
        p = self.p
        request_id = p.get_id("request")
        segment_id = p.get_id("segment")
        p = p.goto_research_team()
        for person in self.team[1:]:
            p = p.goto_role(2).delete().ok()
            self.flag_deleted_approval(person["huid"], True)
        # while p.people_count > 1:
        #     p = p.goto_role(2).delete().ok()
        p = p.goto_request(segment_id, request_id)
        self.p = p
        # reset the internal variable
        self.team = self.team[:1]

    def create_request(self, title, tub="520"):
        self.tub = tub
        self.org = data.random_orgs(1, tub=tub)[0]
        self.p = rgs(self.p, req_with_team(self.pi_huid, self.team[1:], title, org=self.org))
        # p = rgs(self.p, req_with_team(self.pi_huid, self.team[1:], title))
        self.segment_id = self.p.get_id("segment")
        print "Created segment {}".format(self.p.get_id("segment"))

    def change_request_pi(self):
        pi = data.random_huid_with_name()
        self.pi_huid = pi[0]
        self.pi_name = pi[1]
        self.team[0] = {
            "huid": self.pi_huid,
            "name": self.pi_name,
            "role": "Principal Investigator",
            "key": "true",
            "investigator": "true",
            "hs": "false",
            "university": pi[2]
        }
        p = self.p
        p = p.edit_info()
        p.pi = pi[0]
        p = p.ok()

    def change_request_org(self, tub):
        org = data.random_orgs(1, tub=tub)[0]
        self.tub = tub
        self.org = org
        p = self.p.edit_info()
        p.org = org
        p = p.ok()

    def create_to_confirm(self, title, tub="520", submit_oar=False):
        self.create_request(title, tub)
        if submit_oar is True:
            self.submit_oar_create()
        self.assert_approvals()
        p = initiate(self.p)
        p = submit(p)
        p = log_notice(p)
        p = p.project_snapshot.goto_segment_home()
        p = p.confirm_research_team()
        self.p = p

    def change_confirm_flags(self):
        p = self.p
        for i, person in enumerate(self.team[1:], 2):
            current_flag = person["investigator"]
            new_flag = "true" if current_flag == "false" else "false"
            self.team[i - 1]["investigator"] = new_flag
            self.flag_deleted_approval(person["huid"], False)
            p.person(i).investigator = map_value(new_flag)

    def add_person_at_confirm(self, key, investigator, university):
        """
        Expects to already be on SCR_0645
        Does not set commitment % or sponsor commitment flags
        """
        new_person = research_team_record(key, investigator, university)
        new_person["source"] = "segment"
        self.team.append(new_person)

        p = self.p
        p.new_person = new_person["huid"]
        count = p.person_count
        p.person(count).role = new_person["role"]
        p.person(count).key = map_value(new_person["key"])
        p.person(count).investigator = map_value(new_person["investigator"])
        p.person(count).human_subjects = map_value(new_person["hs"])
        self.p = p

    def add_standard_team_at_confirm(self):
        for person in standard_team:
            self.add_person_at_confirm(**person)

    def delete_team_at_confirm(self):
        p = self.p
        for person in self.team[1:]:
            p.person(2).delete()
            self.flag_deleted_approval(person["huid"], False)
        self.team = self.team[:1]

    def confirm_team(self):
        """
        From request home
        """
        p = self.p
        if p.scr == "SCR0115":
            p = initiate(p)
            p = submit(p)
            p = log_notice(p)
            p = confirm_team(p)
        if p.scr == "SCR0645":
            fill_commitments(p)
            p = p.ok()
        self.p = p

    def create_confirmed(self, title, tub="520", submit_oar=False):
        """
        Create a confirmed research team
        """
        self.create_to_confirm(title, tub, submit_oar)
        self.confirm_team()

    ###
    # EDIT TEAM METHODS
    ###
    def start_edit(self):
        p = self.p.goto_research_team()
        p = p.edit_team()
        self.p = p

    def finish_edit(self):
        self.p = self.p.ok().back()

    def edit_team_no_change(self):
        self.start_edit()
        self.finish_edit()

    def edit_team_add_person(self, key, investigator, university):
        """
        Assume already on 649
        """
        p = self.p
        person = research_team_record(key, investigator, university)
        person["source"] = "segment"
        self.team.append(person)
        p.add_member = person["huid"]
        count = p.person_count
        p.person(count).role = person["role"]
        p.person(count).key = map_value(person["key"])
        p.person(count).phs = map_value(person["investigator"])
        p.person(count).hs = map_value(person["hs"])
        p.person(count).cal = 10
        p.person(count).effective_date = "1-1-2014"
        p.person(count).sponsor_commitment = "No"

    def edit_team_add_standard_team(self):
        # from segment home
        self.start_edit()
        for person in standard_team:
            self.edit_team_add_person(**person)
        self.finish_edit()

    def edit_team_remove_team(self):
        self.start_edit()
        self.delete_team_at_confirm()
        self.finish_edit()

    def edit_team_change_flags(self):
        pass

    # END

    def submit_oar_create(self):
        from gmas_webdriver.interfaces.oar import submit_oar_create
        submit_oar_create(self.p)

    def get_approvals(self):
        """
        assume on request or segment home
        """
        # p = self.p.goto_approvals()
        approvals = {}
        p = self.p.goto_approvals()
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

            assert oar_count == (1 if (person["investigator"] == "true" and self.tub == "520") else 0)
            assert fcoi_count == (1 if (self.tub != "520" and (person["investigator"] == "true" or person["university"] == "1")) else 0)

        # check on any leftover approvals
        for huid in keys:
            for approval in approvals[huid]:
                # check that this should be here...
                assert approval["id"] in self.deleted_approvals and self.deleted_approvals[approval["id"]]["db_delete"] is False
                # print self.deleted_approvals[approval["id"]]

        self.assert_removal_queue()

    def assert_removal_queue(self):
        local_removals = [approval_id for approval_id in self.deleted_approvals if self.deleted_approvals[approval_id]["queue"] is True]
        from gmas_webdriver.interfaces.oar import removal_queue_for_segment
        database_removals = removal_queue_for_segment(self.segment_id, self.p)
        for removal in local_removals:
            assert removal in database_removals
            database_removals.remove(removal)
        assert len(database_removals) == 0
