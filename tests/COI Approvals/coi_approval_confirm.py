from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples, submit, initiate
from gmas_webdriver.scripts.notice.notice import log_notice
from gmas_webdriver.scenarios import data

people = None
sponsor = None


def request():
    global sponsor
    request = samples.minimal
    request.update({
        "title": samples.add_ts("OAR approval test automation - confirm research team"),
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


class test_coi_confirm_team(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        global p
        p.quit()

    def setUp(self):
        pass

    def tearDown(self):
        global p
        print "Created segment %s" % p.get_id("segment")

    def assertOAR(self):
        self.get_approval_counts()
        for person in people:
            self.assertEqual(people[person]["OAR"], 1 if people[person]["investigator"] == "true" else 0)
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

    def create_to_confirm(self, r):
        global p
        p = rgs(p.global_header.goto_home(), r)
        p = initiate(p)
        p = submit(p)
        p = log_notice(p)
        p = p.project_snapshot.goto_segment_home()
        p = p.confirm_research_team()

    def test_confirm_team_basic(self):
        global p
        r = request()
        init_people(r)
        self.create_to_confirm(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertOAR()

    def test_confirm_team_change_key_flag(self):
        global p
        r = request()
        self.create_to_confirm(r)
        # change flag from nonkey to key
        p.person(4).key = "Yes"
        r["research team"][2]["key"] = "true"
        r["research team"][2]["investigator"] = "true"
        init_people(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertOAR()

    def test_confirm_team_change_investigator_flag(self):
        global p
        r = request()
        self.create_to_confirm(r)
        # change flag from nonkey to key
        p.person(4).investigator = "Yes"
        r["research team"][2]["investigator"] = "true"
        init_people(r)
        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertOAR()

    def test_confirm_team_add_key(self):
        global p
        r = request()
        init_people(r)
        new_person = data.random_huid()[0]
        people[new_person] = {
            "investigator": "true",
            "OAR": 0,
            "FCOI": 0
        }
        self.create_to_confirm(r)

        p.new_person = new_person
        p.person(5).role = "Analyst"
        p.person(5).key = "Yes"
        #p.person(5).investigator = "Analyst"
        p.person(5).human_subjects = "No"

        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertOAR()

    def test_confirm_team_add_nonkey(self):
        global p
        r = request()
        init_people(r)
        new_person = data.random_huid()[0]
        people[new_person] = {
            "investigator": "false",
            "OAR": 0,
            "FCOI": 0
        }
        self.create_to_confirm(r)

        p.new_person = new_person
        p.person(5).role = "Analyst"
        p.person(5).key = "No"
        p.person(5).investigator = "No"
        p.person(5).human_subjects = "No"

        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertOAR()

    def test_confirm_team_add_nonkey_investigator(self):
        global p
        r = request()
        init_people(r)
        new_person = data.random_huid()[0]
        people[new_person] = {
            "investigator": "true",
            "OAR": 0,
            "FCOI": 0
        }
        self.create_to_confirm(r)

        p.new_person = new_person
        p.person(5).role = "Analyst"
        p.person(5).key = "No"
        p.person(5).investigator = "Yes"
        p.person(5).human_subjects = "No"

        count = p.person_count
        for i in range(count):
            person = p.person(i + 1)
            person.cal_effort = "10"
            if i > 0:
                person.sponsor_commitment = "No"
        p = p.ok()
        self.assertOAR()


if __name__ == '__main__':
    sponsor = "nih"
    print "PHS Confirm team"
    unittest.main(verbosity=2, exit=False)

    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_confirm_team("test_confirm_team_change_key_flag"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
