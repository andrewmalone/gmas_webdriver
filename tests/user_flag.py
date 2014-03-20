from gmas_webdriver.setup import init, init_db

db = init_db("gdev")
p = init("Firefox", "gdev")

import scripts.security.user as security
from scripts.person.search import search_by_huid
import database.person as person_query
import database.segment as segment_query
import unittest
from scripts.request.rgs import rgs, samples

# new huid not in persons...
main_huid = "10550475"
huid = person_query.get_huid_not_in_persons(db)
person_id = None
name = None
team = "GMAS^Team-- university wide"
segment = segment_query.get_active_segment(db)
role = "Observer"

def setUpModule():
    global p, person_id, name
    # get the person id
    p = search_by_huid(p, huid)
    # go back and forth!
    p = p.goto_last_breadcrumb().click_first_result()
    person_id = p.get_person_id()
    name = p.full_name

def page(p):
    return p.get_current_page()[0:7]

class testUserFlag(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        global p
        self.p = p

    def setUp(self):
        self.p = self.p.test_login(main_huid)

    def test_01_empty_user(self):
        p = self.p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_02_new_flagged_user(self):
        p = security.flag_user(self.p, huid, "Yes")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_03_add_user_to_standing_team(self):
        p = security.add_to_standing_team(self.p, huid, team)
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0270")

    def test_04_unflag_user(self):
        p = security.flag_user(self.p, huid, "No")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_05_remove_user_from_standing_team(self):
        p = security.flag_user(self.p, huid, "Yes")
        p = security.remove_from_standing_team(p, huid, team)
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_06_add_user_to_project_team(self):
        p = security.add_to_project_team(self.p, huid, segment, role)
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0270")

    def test_07_unflag_user(self):
        p = security.flag_user(self.p, huid, "No")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_08_remove_user_from_project_team(self):
        p = security.flag_user(self.p, huid, "Yes")
        p = security.remove_from_project_team(p, huid, segment)
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_09_add_user_as_pi(self):
        f = samples.minimal
        f.update({
                "pi": huid,
                "title": "User flag unit test"
            })
        p = rgs(self.p, f)
        # get the request/segment id to get back here later
        
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0646")

    def test_10_unflag_user(self):
        p = security.flag_user(self.p, huid, "No")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def xtest_11_remove_user_as_pi(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)