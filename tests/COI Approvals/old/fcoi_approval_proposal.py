from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples
from gmas_webdriver.scenarios import data

sponsor = None
people = None
org = "00100"


def request():
    request = samples.minimal
    request.update({
        "title": samples.add_ts("FCOI approval test automation"),
        "pi": data.random_fcoi_university_policy()[0],
        "org": org,
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

    def test_rgs_phs(self):
        global p
        r = request()
        r["sponsor"] = "nih"
        p = rgs(p, r)
        init_people(r)
        self.assertFCOI_PHS()

    def test_rgs_nonphs(self):
        global p
        r = request()
        r["sponsor"] = "egg"
        p = rgs(p, r)
        init_people(r)
        self.assertFCOI_nonPHS()

    def test_add_after_rgs_phs(self):
        global p
        r = request()
        r["sponsor"] = "nih"
        r["pi"] = data.random_fcoi_not_university_policy()[0]
        team = r["research team"]
        r["research team"] = []
        p = rgs(p, r)
        init_people(r)
        people[r["pi"]]["university"] = "false"
        self.assertFCOI_PHS()

        # add the team back!
        for person in team:
            add_person(person)
        self.assertFCOI_PHS()

    def test_add_after_rgs_nonphs(self):
        global p
        r = request()
        r["sponsor"] = "egg"
        r["pi"] = data.random_fcoi_not_university_policy()[0]
        team = r["research team"]
        r["research team"] = []
        p = rgs(p, r)
        init_people(r)
        people[r["pi"]]["university"] = "false"
        self.assertFCOI_nonPHS()

        # add the team back!
        for person in team:
            add_person(person)
        self.assertFCOI_nonPHS()


    # def test_02_change_to_key(self):
    #     global p
    #     p = p.goto_research_team()
    #     p = p.goto_role(4)
    #     p = p.edit_personnel()
    #     p.set_key("true")
    #     p.appt = "12"
    #     request["research team"][2]["key"] = "true"
    #     request["research team"][2]["investigator"] = "true"
    #     init_people()
    #     p = p.ok().back(2)
    #     self.assertOAR()

    # def test_03_change_to_investigator(self):
    #     global p
    #     p = p.goto_research_team()
    #     p = p.goto_role(5)
    #     p = p.edit_personnel()
    #     p.phs = "true"
    #     p.appt = "12"
    #     request["research team"][3]["investigator"] = "true"
    #     init_people()
    #     p = p.ok().back(2)
    #     self.assertOAR()

    # def test_04_add_key_hms(self):
    #     global p
    #     add_person(data.random_huid()[0], key="true")
    #     self.assertOAR()

    # def test_05_add_nonkey_hms(self):
    #     global p
    #     add_person(data.random_huid()[0], key="false", investigator="false")
    #     self.assertOAR()

    # def test_06_add_nonkey_investigator_hms(self):
    #     global p
    #     add_person(data.random_huid()[0], key="false", investigator="true")
    #     self.assertOAR()

    # def test_07_change_pi_hms(self):
    #     global p
    #     p = p.edit_info()
    #     huid = data.random_huid()[0]
    #     people[huid] = {
    #         "investigator": "true"
    #     }
    #     p.pi = huid
    #     p = p.ok()
    #     self.assertOAR()


if __name__ == '__main__':
    org = "23515"
    unittest.main(verbosity=2, exit=False)
    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_approval_creation("test_01_hms_phs_proposal_rgs"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
