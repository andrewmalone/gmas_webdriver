from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples, submit, initiate, supplement
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

supplement_data = {
    # SCR_0473
    "retro": "false",
    # SCR_0089
    "rfp": "false",
    "subs": "false",
    "ifi": "false",
    # SCR_0231
    "due_date": "1/1/08",
    "due_date_type": "2401",
    "copies": "1",
    # SCR_0090
    # SCR_0229
    "estimated_cost": "50000",  # optional
    "cost_share": "false",
    "matching": "false",
    "admin_salary": "false",
    "on_campus": "true",
    # SCR_0091, #SCR_0092
    # SCR_0228, #SCR_0094
    "ifi_list": [  # optional
        {
            "org": "31240",
            "pi": "03750001"
            # admin
        }
    ],
    # SCR_0098
    "research team": [  # optional
    ],
    # SCR_0097
    "human_subjects": "false",
    "animals": "false",
    "protocol": "false",
    "biohazards": "false",
    "stem_cells": "false",
    "foreign": "false",
    "add_staff": "false",
    "use_of_name": "false",
    "appt_exp": "false",
    "appt_exp_option": "transfer institution",  # only required if appt_exp is true
    "appt_exp_comment": "Other"  # only required if appt_exp_option is "other"
}


def request():
    global sponsor
    request = samples.minimal
    request.update({
        "title": samples.add_ts("OAR supplement approval test automation"),
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
            # 10604826
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


def add_person_supplement(huid, key="true", investigator="true"):
    global supplement_data, people
    supplement_data["research team"].append({
        "huid": huid,
        "role": "Consultant",
        "key": key,
        "investigator": investigator,
        "hs": "false"
        })
    people[huid] = {
        "investigator": investigator,
        "OAR": 0,
        "FCOI": 0,
        "added": True
    }


class test_coi_supplement(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        global p
        # p.quit()

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

    def assertOARSegment(self):
        global p
        if p.scr != "SCR0104":
            p = p.project_snapshot.goto_segment_home()
        self.get_approval_counts()
        for person in people:
            expected_oar = 0
            if people[person]["investigator"] == "true":
                if "added" in people[person] and people[person]["added"] is True:
                    expected_oar = 1
                else:
                    expected_oar = 2
            self.assertEqual(people[person]["OAR"], expected_oar)
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

    def test_supplement_basic(self):
        global p
        p = supplement(p, supplement_data)
        self.assertOAR()
        self.assertOARSegment()

    def test_add_people(self):
        global p
        p = supplement(p, supplement_data)
        add_person(data.random_huid()[0], key="true")
        add_person(data.random_huid()[0], key="false", investigator="false")
        add_person(data.random_huid()[0], key="false", investigator="true")
        self.assertOAR()
        self.assertOARSegment()

    def test_add_people_rgs(self):
        global p
        add_person_supplement(data.random_huid()[0], key="true")
        add_person_supplement(data.random_huid()[0], key="false", investigator="false")
        add_person_supplement(data.random_huid()[0], key="false", investigator="true")
        p = supplement(p, supplement_data)
        self.assertOAR()
        self.assertOARSegment()

    def test_change_flags(self):
        global p
        p = supplement(p, supplement_data)
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
        self.assertOAR()

    def test_award_supplement(self):
        global p
        p = supplement(p, supplement_data)
        add_person(data.random_huid()[0], key="true")
        add_person(data.random_huid()[0], key="false", investigator="false")
        add_person(data.random_huid()[0], key="false", investigator="true")
        p = initiate(p)
        p = submit(p)
        p = log_notice(p)
        p = p.review_completed()
        p = awarding_revision(p, {}, minimal=True, notification=False)
        p = p.back(2)
        self.assertOARSegment()

if __name__ == '__main__':
    sponsor = "nih"
    unittest.main(verbosity=2, exit=False)

    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_confirm_team("test_confirm_team_change_key_flag"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
