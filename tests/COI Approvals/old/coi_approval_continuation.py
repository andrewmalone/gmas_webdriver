from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples, submit, initiate, continuation
from gmas_webdriver.scripts.revision.revision import awarding_revision
from gmas_webdriver.scripts.notice.notice import log_notice
from gmas_webdriver.scenarios import data

people = None
sponsor = None

revision_data = {
    # 328
    "funding_instrument": "Grant",
    "payment_method": "Check",
    "arra": "false",
    "equipment": "false",
    "agency": "false",
    "ia": "false",
    "snap": "false",
    "cfda": "1234",
    "prime award": "prime123",
    "foreign": "false",
    "awarded_dates": [  # optional
        {
            "period": 1,
            "ob_start": "ant_start",
            "ob_end": "ant_end"
        }
    ]
}

continuation_data = {
    # SCR_0472
    "retro": "false",
    # SCR_0231
    "due_date": "1/1/08",
    "due_date_type": "2401",
    "copies": "1",
    # SCR_0461
    "q1": "false",
    "q2": "false",
    "q3": "false",
    # SCR_0097
    "human_subjects": "false",
    "animals": "false",
    "biohazards": "false",
    "stem_cells": "false",
    "foreign": "false",
    "add_staff": "false",
    "use_of_name": "false",
    "appt_exp": "false",
    "cost_share": "false",
    "matching": "false",
    "admin_salary": "false",
    "protocol": "false"
}


def request():
    global sponsor
    request = samples.minimal
    request.update({
        "title": samples.add_ts("OAR continuation approval test automation"),
        "org": "45317",
        "pi": data.random_huid()[0],
        "sponsor": sponsor,
        #"project_type": "Fellowship",
        #"mentor": "03750002",
        #"mentor_hs": "false",
        #"mentor_key": "true",
        "periods": "4",
        "research team": [
            {
                "huid": data.random_huid()[0],
                "role": "Consultant",
                "key": "true",
                "investigator": "true",
                "hs": "false"
            },
            {
                "huid": data.random_huid()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "true",
                "hs": "false"
            },
            {
                "huid": data.random_huid()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "false",
                "hs": "false"
            },
            {
                "huid": data.random_huid()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "false",
                "hs": "false"
            }
        ]
    })
    return request


def init_people(request):
    global people
    people = {}
    people[request["pi"]] = {
        "investigator": "true",
        "OAR": 0,
        "FCOI": 0
    }
    for person in request["research team"]:
        people[person["huid"]] = {
            "investigator": person["investigator"],
            "OAR": 0,
            "FCOI": 0
        }


def reset_people():
    global people
    for person in people:
        people[person]["OAR"] = 0
        people[person]["FCOI"] = 0


def add_person(huid, key="true", investigator="true"):
    global p
    p = p.goto_research_team().add_team_member()
    p.name = huid
    p.human_subjects = "false"
    p.role = "Analyst"
    p.set_key(key)
    if key == "false":
        p.phs = investigator
    p.set_effort("0")
    p.appt = "12"
    p = p.ok().back()
    global people
    people[huid] = {
        "investigator": investigator,
        "OAR": 0,
        "FCOI": 0,
        "added": True
    }


class test_coi_continuation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        global p
        p.quit()

    def setUp(self):
        global p
        r = request()
        init_people(r)
        self.request = r
        p = rgs(p.global_header.goto_home(), r)
        p = initiate(p)
        p = submit(p)
        p = log_notice(p)
        p = p.project_snapshot.goto_segment_home()
        p = p.confirm_research_team()
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        p = p.goto_notices()
        p = p.goto_first_notice()
        p = p.review_completed()
        p = awarding_revision(p, revision_data, notification=False)
        p = p.project_snapshot.goto_segment_home()
        self.segment = p.get_id("segment")
        print "Created segment %s" % self.segment

        if p.scr != "SCR0104":
            p = p.goto_segment(self.segment)

    def tearDown(self):
        pass

    def assertOAR(self):
        self.get_approval_counts()
        for person in people:
            self.assertEqual(people[person]["OAR"], 1 if people[person]["investigator"] == "true" else 0)
            self.assertEqual(people[person]["FCOI"], 0)

    def assertNone(self):
        self.get_approval_counts()
        for person in people:
            self.assertEqual(people[person]["OAR"], 0)
            self.assertEqual(people[person]["FCOI"], 0)

    def get_approval_counts(self):
        #p = self.p
        global p
        reset_people()
        p = p.goto_approvals()
        for approval in p.approvals:
            # OAR Conflict of Interest
            # Conflict of Interest
            if approval.type == "Conflict of Interest":
                people[approval.huid]["FCOI"] += 1
            if approval.type == "OAR Conflict of Interest":
                people[approval.huid]["OAR"] += 1
        p = p.back()

    def test_continuation_basic(self):
        global p
        p = continuation(p, continuation_data)
        self.assertNone()

    def test_add_people(self):
        global p
        p = continuation(p, continuation_data)
        add_person(data.random_huid()[0], key="true")
        add_person(data.random_huid()[0], key="false", investigator="false")
        add_person(data.random_huid()[0], key="false", investigator="true")
        self.assertNone()

    def test_change_flags(self):
        global p
        p = continuation(p, continuation_data)
        p = p.goto_research_team()
        p = p.goto_role(4)
        p = p.edit_personnel()
        p.set_key("true")
        p.appt = "12"
        self.request["research team"][2]["key"] = "true"
        self.request["research team"][2]["investigator"] = "true"
        p = p.ok().back()
        p = p.goto_role(5)
        p = p.edit_personnel()
        p.phs = "true"
        p.appt = "12"
        self.request["research team"][3]["investigator"] = "true"
        init_people(self.request)
        p = p.ok().back(2)
        self.assertNone()

    def test_award_continuation(self):
        global p
        p = continuation(p, continuation_data)
        add_person(data.random_huid()[0], key="true")
        add_person(data.random_huid()[0], key="false", investigator="false")
        add_person(data.random_huid()[0], key="false", investigator="true")
        p = initiate(p)
        p = submit(p)
        p = log_notice(p)
        p = p.review_completed()
        p = awarding_revision(p, {}, minimal=True, notification=False)
        p = p.back(2)
        self.assertOAR()

if __name__ == '__main__':
    sponsor = "nih"
    #unittest.main(verbosity=2, exit=False)

    suite = unittest.TestSuite()
    suite.addTest(test_coi_continuation("test_award_continuation"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
