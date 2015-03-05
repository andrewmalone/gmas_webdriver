from COI_Confirm import COI_Confirm
from common import standard_team, research_team_record, map_value


class COI_Edit(COI_Confirm):
    def start_edit(self):
        p = self.p.goto_research_team()
        p = p.edit_team()
        self.p = p

    def finish_edit(self):
        self.p = self.p.ok().back()

    def edit_team_no_change(self):
        self.start_edit()
        self.finish_edit()

    def edit_team_add_person(self, key, investigator, university):
        """
        Assume already on 649
        """
        p = self.p
        person = research_team_record(key, investigator, university)
        person["source"] = "segment"
        self.team.append(person)
        p.add_member = person["huid"]
        count = p.person_count
        p.person(count).role = person["role"]
        p.person(count).key = map_value(person["key"])
        p.person(count).phs = map_value(person["investigator"])
        p.person(count).hs = map_value(person["hs"])
        p.person(count).cal = 10
        p.person(count).effective_date = "1-1-2014"
        p.person(count).sponsor_commitment = "No"

    def edit_team_add_standard_team(self):
        # from segment home
        self.start_edit()
        for person in standard_team:
            self.edit_team_add_person(**person)
        self.finish_edit()

    def edit_team_remove_team(self):
        self.start_edit()
        self.delete_team_at_confirm()
        self.finish_edit()

    def edit_team_change_flags(self):
        pass
