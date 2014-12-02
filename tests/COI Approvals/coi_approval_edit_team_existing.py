from gmas_webdriver.setup import init, init_db
p = init("Chrome", "gdev", True)

import unittest
from gmas_webdriver.scenarios import data
from gmas_webdriver.database import db
import random

people = {}


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
    if key == "No":
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


class test_coi_edit_team_existing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        database = init_db("gdev11")
        query = """
        select
          s.segment_id
        from
          segments s
          left join approval_requirements a on s.segment_id = a.segment_id and a.approval_type_id = 2022
          join faculty_involvements fi on fi.segment_id = s.segment_id and fi.end_date is null
          join faculty_research_persons frp on fi.faculty_involvement_id = frp.faculty_involvement_id
            and frp.end_date is null
            and frp.created_by_request_id is null
          join rf_segment_statuses rss on rss.segment_status_id = s.segment_status_id
          join rf_orgs org on fi.org = org.org
        where
          rss.description = 'Active'
          and org.tub = '520'
        group by
          s.segment_id
        having
          count(distinct a.approval_requirement_id) = 0
          and count(distinct frp.person_id) > 2
          """
        self.segments = db.get_list(database, query)

    @classmethod
    def tearDownClass(self):
        global p
        #p.quit()

    def setUp(self):
        global p
        self.segment = random.choice(self.segments)
        self.segments.remove(self.segment)
        p = p.goto_segment(self.segment)

    def tearDown(self):
        print "Segment {0}".format(self.segment)

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

    def test_edit_basic(self):
        global p
        p = p.goto_research_team()
        p = p.edit_team()
        p = p.ok()
        p = p.back()
        p = p.goto_approvals()
        oar_count = 0
        for approval in p.approvals:
            if approval.type == "OAR Conflict of Interest":
                oar_count += 1
        self.assertEqual(oar_count, 0)

    def test_add_people(self):
        global p
        p = p.goto_research_team()
        p = p.edit_team()
        add_person(data.random_huid()[0], key="true")
        add_person(data.random_huid()[0], key="false", investigator="false")
        add_person(data.random_huid()[0], key="false", investigator="true")
        p = p.ok()
        p = p.back()
        p = p.goto_approvals()

        for approval in p.approvals:
            if approval.type == "OAR Conflict of Interest":
                self.assertIn(approval.huid, people)
                self.assertEqual(people[approval.huid]["investigator"], "true")
                people[approval.huid]["OAR"] += 1
            if approval.type == "Conflict of Interest":
                self.assertNotIn(approval.huid, people)

        for person in people:
            self.assertEqual(people[person]["OAR"], 1 if people[person]["investigator"] == "true" else 0)

    def _test_change_flags(self):
        global p
        p = p.goto_research_team()
        p = p.edit_team()
        p.row(4).key = "Yes"
        self.request["research team"][2]["key"] = "true"
        self.request["research team"][2]["investigator"] = "true"
        p.row(5).phs = "Yes"
        self.request["research team"][3]["investigator"] = "true"
        init_people(self.request)
        p = p.ok()
        p = p.back()
        self.assertOAR()

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
