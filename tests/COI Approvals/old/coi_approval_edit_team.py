from gmas_webdriver.setup import init
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scripts.request import rgs, samples, submit, initiate
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


def request():
    global sponsor
    request = samples.minimal
    request.update({
        "title": samples.add_ts("OAR edit team test automation"),
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
    key = "Yes" if key == "true" else "No"
    investigator = "Yes" if investigator == "true" else "No"
    p.add_member = huid
    r = p.row(p.count_rows())
    r.role = "Consultant"
    r.key = key
    r.phs = investigator
    r.hs = "No"
    r.cal = 10
    r.effective_date = "1-1-2014"
    r.sponsor_commitment = "No"

    global people
    people[huid] = {
        "investigator": "true" if investigator == "Yes" else "false",
        "OAR": 0,
        "FCOI": 0,
        "added": True
    }


class test_coi_edit_team(unittest.TestCase):
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

        if p.scr != "SCR0104":
            p = p.goto_segment(self.segment)

    def tearDown(self):
        print "Created segment %s" % self.segment
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

    def test_edit_basic(self):
        global p
        p = p.goto_research_team()
        p = p.edit_team()
        p = p.ok()
        p = p.back()
        self.assertOAR()

    def test_add_people(self):
        global p
        p = p.goto_research_team()
        p = p.edit_team()
        add_person(data.random_huid()[0], key="true")
        add_person(data.random_huid()[0], key="false", investigator="false")
        add_person(data.random_huid()[0], key="false", investigator="true")
        p = p.ok()
        p = p.back()
        self.assertOAR()

    def test_change_flags(self):
        global p
        p = p.goto_research_team()
        p = p.edit_team()
        p.row(4).key = "Yes"
        p.row(4).phs = "Yes"
        self.request["research team"][2]["key"] = "true"
        self.request["research team"][2]["investigator"] = "true"
        p.row(5).phs = "Yes"
        self.request["research team"][3]["investigator"] = "true"
        init_people(self.request)
        p = p.ok()
        p = p.back()
        self.assertOAR()

if __name__ == '__main__':
    sponsor = "nih"
    unittest.main(verbosity=2, exit=False)
    #test_coi_edit_team().setup()
    #setup()

    # suite = unittest.TestSuite()
    # suite.addTest(test_coi_confirm_team("test_confirm_team_change_key_flag"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
