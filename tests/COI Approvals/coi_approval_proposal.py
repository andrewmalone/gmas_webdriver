from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples
from gmas_webdriver.scenarios import data

people = None
request = samples.minimal
request.update({
    "title": samples.add_ts("OAR approval test automation"),
    "org": "45317",
    "pi": data.random_huid()[0],
    "sponsor": "egg",
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


def init_people():
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
        "FCOI": 0
    }

init_people()


class test_coi_approval_creation(unittest.TestCase):
    def setUp(self):
        pass

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

    def test_01_hms_phs_proposal_rgs(self):
        global p
        p = rgs(p, request)
        self.assertOAR()

    def test_02_change_to_key(self):
        global p
        p = p.goto_research_team()
        p = p.goto_role(4)
        p = p.edit_personnel()
        p.set_key("true")
        p.appt = "12"
        request["research team"][2]["key"] = "true"
        request["research team"][2]["investigator"] = "true"
        init_people()
        p = p.ok().back(2)
        self.assertOAR()

    def test_03_change_to_investigator(self):
        global p
        p = p.goto_research_team()
        p = p.goto_role(5)
        p = p.edit_personnel()
        p.phs = "true"
        p.appt = "12"
        request["research team"][3]["investigator"] = "true"
        init_people()
        p = p.ok().back(2)
        self.assertOAR()

    def test_04_add_key_hms(self):
        global p
        add_person(data.random_huid()[0], key="true")
        self.assertOAR()

    def test_05_add_nonkey_hms(self):
        global p
        add_person(data.random_huid()[0], key="false", investigator="false")
        self.assertOAR()

    def test_06_add_nonkey_investigator_hms(self):
        global p
        add_person(data.random_huid()[0], key="false", investigator="true")
        self.assertOAR()

    def test_07_change_pi_hms(self):
        global p
        p = p.edit_info()
        huid = data.random_huid()[0]
        people[huid] = {
            "investigator": "true"
        }
        p.pi = huid
        p = p.ok()
        self.assertOAR()


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_approval_creation("test_01_hms_phs_proposal_rgs"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
