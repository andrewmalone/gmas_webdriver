from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples, submit, initiate
from gmas_webdriver.scripts.notice.notice import log_notice
from gmas_webdriver.scenarios import data

sponsor = None
people = None
org = "00100"


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


class test_coi_approval_creation(unittest.TestCase):
    def setUp(self):
        global p
        if p.scr != "SCR0270":
            p = p.global_header.goto_home()

    def tearDown(self):
        global p
        print "Created segment %s" % p.get_id("segment")

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

    def create_to_confirm(self, r):
        global p
        p = rgs(p, r)
        p = initiate(p)
        p = submit(p)
        p = log_notice(p)
        p = p.project_snapshot.goto_segment_home()
        p = p.confirm_research_team()

    def _test_confirm_team_basic_phs(self):
        global p
        r = request("nih")
        init_people(r)
        self.create_to_confirm(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertFCOI_PHS()

    def _test_confirm_team_basic_nonphs(self):
        global p
        r = request("egg")
        init_people(r)
        self.create_to_confirm(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertFCOI_nonPHS()

    def test_confirm_team_change_key_flag_phs(self):
        global p
        r = request("nih")
        self.create_to_confirm(r)
        # change flag from nonkey to key
        p.person(7).key = "Yes"
        r["research team"][5]["key"] = "true"
        r["research team"][5]["investigator"] = "true"
        init_people(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertFCOI_PHS()

    def test_confirm_team_change_key_flag_nonphs(self):
        global p
        r = request("egg")
        self.create_to_confirm(r)
        # change flag from nonkey to key
        p.person(7).key = "Yes"
        r["research team"][5]["key"] = "true"
        r["research team"][5]["investigator"] = "true"
        init_people(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertFCOI_nonPHS()


if __name__ == '__main__':
    org = "31570"
    unittest.main(verbosity=2, exit=False)
    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_approval_creation("test_01_hms_phs_proposal_rgs"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
