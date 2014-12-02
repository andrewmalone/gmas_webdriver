from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples, submit, initiate, supplement
from gmas_webdriver.scripts.revision.revision import awarding_revision
from gmas_webdriver.scripts.notice.notice import log_notice
from gmas_webdriver.scenarios import data

sponsor = None
people = None
org = "00100"

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


def request(sponsor="nih"):
    request = samples.minimal
    request.update({
        "title": samples.add_ts("FCOI approval test automation"),
        "pi": data.random_fcoi_university_policy()[0],
        "org": org,
        "sponsor": sponsor,
        #"project_type": "Fellowship",
        #"mentor": "03750002",
        #"mentor_hs": "false",
        #"mentor_key": "true",
        "periods": "4",
        "research team": [
            {
                # key person, univ policy
                "huid": data.random_fcoi_university_policy()[0],
                "role": "Consultant",
                "key": "true",
                "investigator": "true",
                "hs": "false",
                "university": "true"
            },
            {
                # key person, not univ policy
                "huid": data.random_fcoi_not_university_policy()[0],
                "role": "Consultant",
                "key": "true",
                "investigator": "true",
                "hs": "false",
                "university": "false"
            },
            {
                # nonkey investigator, univ policy
                "huid": data.random_fcoi_university_policy()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "true",
                "hs": "false",
                "university": "true"
            },
            {
                # nonkey investigator, not univ policy
                "huid": data.random_fcoi_not_university_policy()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "true",
                "hs": "false",
                "university": "false"
            },
            {
                # nonkey univ policy
                "huid": data.random_fcoi_university_policy()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "false",
                "hs": "false",
                "university": "true"
            },
            {
                # nonkey, not univ policy
                "huid": data.random_fcoi_not_university_policy()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "false",
                "hs": "false",
                "university": "false"
            },
            {
                # nonkey, not univ policy
                "huid": data.random_fcoi_not_university_policy()[0],
                "role": "Consultant",
                "key": "false",
                "investigator": "false",
                "hs": "false",
                "university": "false"
            }
        ]
    })
    return request


def init_people(request):
    global people
    people = {}
    people[request["pi"]] = {
        "investigator": "true",
        "university": "true",
        "key": "true",
        "OAR": 0,
        "FCOI": 0
    }
    for person in request["research team"]:
        people[person["huid"]] = {
            "investigator": person["investigator"],
            "university": person["university"],
            "key": person["key"],
            "OAR": 0,
            "FCOI": 0
        }


def reset_people():
    global people
    for person in people:
        people[person]["OAR"] = 0
        people[person]["FCOI"] = 0


def add_person(person):
    global p
    p = p.goto_research_team().add_team_member()
    p.name = person["huid"]
    p.human_subjects = "false"
    p.role = "Analyst"
    p.set_key(person["key"])
    if person["key"] == "false":
        p.phs = person["investigator"]
    p.set_effort("0")
    p.appt = "12"
    p = p.ok().back()
    global people
    people[person["huid"]] = {
        "investigator": person["investigator"],
        "university": person["university"],
        "OAR": 0,
        "FCOI": 0
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


class test_fcoi_approval_supplement(unittest.TestCase):
    def setUp(self):
        global p
        if p.scr != "SCR0270":
            p = p.global_header.goto_home()

    def tearDown(self):
        print "Created segment %s" % self.segment

    @classmethod
    def tearDownClass(self):
        global p
        # p.quit()

    def assertFCOI_PHS(self):
        self.get_approval_counts()
        for person in people:
            fcoi = 0
            if people[person]["investigator"] == "true" or people[person]["university"] == "true":
                fcoi = 1
            self.assertEqual(people[person]["OAR"], 0)
            self.assertEqual(people[person]["FCOI"], fcoi)

    def assertFCOI_nonPHS(self):
        self.get_approval_counts()
        for person in people:
            fcoi = 0
            if people[person]["university"] == "true":
                fcoi = 1
            self.assertEqual(people[person]["OAR"], 0)
            self.assertEqual(people[person]["FCOI"], fcoi)

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

    def create_active(self, r):
        global p
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
        # print "Created segment %s" % self.segment

    def test(self):
        global p
        r = request("nih")
        self.create_active(r)
        p = supplement(p, supplement_data)
        self.assertNone()


if __name__ == '__main__':
    org = "31570"
    unittest.main(verbosity=2, exit=False)
    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_approval_creation("test_01_hms_phs_proposal_rgs"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
