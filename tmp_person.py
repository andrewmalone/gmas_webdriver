from gmas_webdriver.setup import init
import scripts.security.security as security
from scripts.person.search import search_by_huid
import unittest

p = init("Firefox", "gmasdev.cadm", True)
# new huid not in persons...
main_huid = "10550475"
huid = "50877396"
person_id = None
name = None
team = "GMAS^Team-- university wide"
segment = 16625406

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
        self.p.test_login(main_huid)

    def test_00_empty_user(self):
        p = self.p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_01_new_flagged_user(self):
        p = security.flag_user(self.p, huid, "Yes")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_02_add_user_to_standing_team(self):
        p = security.add_to_standing_team(self.p, huid, team)
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0270")

    def test_03_unflag_user(self):
        p = security.flag_user(self.p, huid, "No")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_04_remove_user_from_standing_team(self):
        p = security.flag_user(self.p, huid, "Yes")
        p = security.remove_from_standing_team(p, huid, team)
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_05_add_user_to_project_team(self):
        p = self.p.goto_segment(segment).goto_admin_team()
        p = p.goto_role("Department Administrator")
        p = p.add()
        p.name = huid
        p = p.search()
        p.select_first()
        p = p.ok()
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0270")

    def test_06_unflag_user(self):
        p = security.flag_user(self.p, huid, "No")
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

    def test_07_remove_user_from_project_team(self):
        p = security.flag_user(self.p, huid, "Yes")
        p = p.goto_segment(segment).goto_admin_team()
        p = p.goto_role("Department Administrator")
        p.select_name(name)
        p = p.remove()
        p = p.test_login(huid)
        self.assertEqual(page(p), "SCR0626")

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)