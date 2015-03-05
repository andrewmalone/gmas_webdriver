from COI_Initial import COI_Initial
from gmas_webdriver.scripts.request import initiate, submit
from gmas_webdriver.scripts.notice import log_notice
from gmas_webdriver.scripts.revision.revision import awarding_revision
from gmas_webdriver.scripts.research_team import confirm_team, fill_commitments
from common import map_value, research_team_record, standard_team


class COI_Confirm(COI_Initial):
    def create_to_confirm(self, title, tub="520", submit_oar=False):
        self.create_request(title, tub)
        if submit_oar is True:
            self.submit_oar_create()
        self.assert_approvals()
        p = initiate(self.p)
        p = submit(p)
        p = log_notice(p)
        p = p.project_snapshot.goto_segment_home()
        p = p.confirm_research_team()
        self.p = p

    def change_confirm_flags(self):
        p = self.p
        for i, person in enumerate(self.team[1:], 2):
            current_flag = person["investigator"]
            new_flag = "true" if current_flag == "false" else "false"
            self.team[i - 1]["investigator"] = new_flag
            self.flag_deleted_approval(person["huid"], False)
            p.person(i).investigator = map_value(new_flag)

    def add_person_at_confirm(self, key, investigator, university):
        """
        Expects to already be on SCR_0645
        Does not set commitment % or sponsor commitment flags
        """
        new_person = research_team_record(key, investigator, university)
        new_person["source"] = "segment"
        self.team.append(new_person)

        p = self.p
        p.new_person = new_person["huid"]
        count = p.person_count
        p.person(count).role = new_person["role"]
        p.person(count).key = map_value(new_person["key"])
        p.person(count).investigator = map_value(new_person["investigator"])
        p.person(count).human_subjects = map_value(new_person["hs"])
        self.p = p

    def add_standard_team_at_confirm(self):
        for person in standard_team:
            self.add_person_at_confirm(**person)

    def delete_team_at_confirm(self):
        p = self.p
        for person in self.team[1:]:
            p.person(2).delete()
            if "source" in person and person["source"] == "segment":
                db_delete = True
            else:
                db_delete = False
            self.flag_deleted_approval(person["huid"], db_delete)
        self.team = self.team[:1]

    def confirm_team(self):
        """
        From request home
        """
        p = self.p
        if p.scr == "SCR0115":
            p = initiate(p)
            p = submit(p)
            p = log_notice(p)
            p = confirm_team(p)
        if p.scr == "SCR0645":
            fill_commitments(p)
            p = p.ok()
        self.p = p

    def create_confirmed(self, title, tub="520", submit_oar=False):
        """
        Create a confirmed research team
        """
        self.create_to_confirm(title, tub, submit_oar)
        self.confirm_team()

    def create_awarded(self, title, tub="520", submit_oar=False):
        """
        Create an awarded project
        """
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
        self.create_to_confirm(title, tub, submit_oar)
        self.confirm_team()
        p = self.p
        p = p.goto_notices()
        p = p.goto_first_notice()
        p = p.review_completed()
        p = awarding_revision(p, revision_data, notification=False)
        p = p.project_snapshot.goto_segment_home()
        self.p = p
