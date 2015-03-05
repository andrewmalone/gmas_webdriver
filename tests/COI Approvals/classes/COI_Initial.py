from COI_Base import COI_Test
from common import research_team_record, standard_team, req_with_team
from gmas_webdriver.scenarios import data
from gmas_webdriver.scripts.request import rgs


class COI_Initial(COI_Test):
    def add_person_after_rgs(self, key, investigator, university=None):
        p = self.p
        # add in GMAS
        person = research_team_record(key, investigator, university)
        p = p.goto_research_team().add_team_member()
        p.name = person["huid"]
        p.human_subjects = person["hs"]
        p.role = person["role"]
        p.set_key(person["key"])
        p.phs = person["investigator"]
        p.set_effort("0")
        p.appt = "12"
        p = p.ok().back()
        self.p = p
        self.team.append(person)

    def add_standard_team_after_rgs(self):
        for person in standard_team:
            self.add_person_after_rgs(**person)

    def change_flag_for_request_person(self, index):
        """
        Change the investigator flag for a person on the team (request!)
        """
        current_flag = self.team[index]["investigator"]
        new_flag = "true" if current_flag == "false" else "false"
        p = self.p.goto_research_team().goto_role(index + 1)
        p = p.edit_personnel()
        p.phs = new_flag
        p.appt = "12"
        self.team[index]["investigator"] = new_flag
        self.flag_deleted_approval(self.team[index]["huid"], True)
        p = p.ok().back(2)
        self.p = p

    def change_all_request_flags(self):
        """
        Flips the investigator flag for all people on the research team (not PI)
        """
        for i in range(1, len(self.team)):
            self.change_flag_for_request_person(i)

    def delete_all_request_people(self):
        """
        Removes everyone from the request research team except the PI
        """
        p = self.p
        request_id = p.get_id("request")
        segment_id = p.get_id("segment")
        p = p.goto_research_team()
        for person in self.team[1:]:
            p = p.goto_role(2).delete().ok()
            self.flag_deleted_approval(person["huid"], True)
        # while p.people_count > 1:
        #     p = p.goto_role(2).delete().ok()
        p = p.goto_request(segment_id, request_id)
        self.p = p
        # reset the internal variable
        self.team = self.team[:1]

    def create_request(self, title, tub="520"):
        self.tub = tub
        self.org = data.random_orgs(1, tub=tub)[0]
        self.p = rgs(self.p, req_with_team(self.pi_huid, self.team[1:], title, org=self.org))
        # p = rgs(self.p, req_with_team(self.pi_huid, self.team[1:], title))
        self.segment_id = self.p.get_id("segment")
        print "Created segment {}".format(self.p.get_id("segment"))

    def change_request_pi(self):
        self.flag_deleted_approval(self.pi_huid, True)
        pi = data.random_huid_with_name()
        self.pi_huid = pi[0]
        self.pi_name = pi[1]
        self.team[0] = {
            "huid": self.pi_huid,
            "name": self.pi_name,
            "role": "Principal Investigator",
            "key": "true",
            "investigator": "true",
            "hs": "false",
            "university": pi[2]
        }
        p = self.p
        p = p.edit_info()
        p.pi = pi[0]
        p = p.ok()

    def change_request_org(self, tub):
        from_HMS = False
        to_HMS = False
        if self.tub == "520" and tub != "520":
            from_HMS = True
        if self.tub != "520" and tub == "520":
            to_HMS = True
        if from_HMS is True or to_HMS is True:
            for person in self.team:
                self.flag_deleted_approval(person["huid"], True)
        org = data.random_orgs(1, tub=tub)[0]
        self.tub = tub
        self.org = org
        p = self.p.edit_info()
        p.org = org
        p = p.ok()
