import pytest
from classes.COI_Initial import COI_Initial
from classes.common import standard_team


class Test_COI_RGS(COI_Initial):
    @pytest.mark.deep
    @pytest.mark.parametrize('team_member', standard_team)
    def test_rgs_individual(self, team_member):
        """
        Add research team people in RGS
        Create one project per person flag combination
        """
        title = "COI_create_test_rgs_individual"
        self.add_person_to_team(**team_member)
        self.create_request(title)
        self.assert_approvals()

    @pytest.mark.shallow
    def test_rgs(self):
        """
        Add research team people in RGS
        Create one project with all configurations of key/investigator flags
        """
        title = "COI_create_test_rgs"
        self.add_standard_team()
        self.create_request(title)
        self.assert_approvals()

    @pytest.mark.shallow
    def test_add_people_after_rgs(self):
        """
        Add people after RGS
        Uses all configurations of key/investigator flags
        """
        title = "COI_test_add_people_after_rgs"
        self.create_request(title)
        self.assert_approvals()
        self.add_standard_team_after_rgs()
        self.assert_approvals()

    @pytest.mark.shallow
    def test_change_flags_after_rgs(self):
        """
        Add people in RGS, then change all investigator flags
        """
        title = "COI change flags after RGS"
        self.add_standard_team()
        self.create_request(title)
        self.assert_approvals()
        self.change_all_request_flags()
        self.assert_approvals()

    @pytest.mark.shallow
    def test_add_after_rgs_and_change_flags(self):
        """
        Add people after RGS, then change all investigator flags
        """
        title = "COI add after rgs and change flags"
        self.create_request(title)
        self.assert_approvals(output=False)
        self.add_standard_team_after_rgs()
        self.assert_approvals()
        self.change_all_request_flags()
        self.assert_approvals()

    @pytest.mark.shallow
    def test_delete_people_from_rgs(self):
        title = "COI Test delete proposal team"
        self.add_standard_team()
        self.create_request(title)
        # self.submit_oar_create()
        self.assert_approvals()
        self.delete_all_request_people()
        self.assert_approvals()

    def test_delete_people_from_after_rgs(self):
        pass

    @pytest.mark.combined
    def test_proposal_combined(self):
        """
        Combined test for most scenarios
        """
        title = "COI Combined proposal test"
        self.add_standard_team()
        self.create_request(title)
        self.submit_oar_create()
        self.assert_approvals()
        self.add_standard_team_after_rgs()
        self.assert_approvals()
        self.change_all_request_flags()
        self.assert_approvals()
        self.delete_all_request_people()
        self.assert_approvals()
        self.change_request_pi()
        self.assert_approvals()

    @pytest.mark.combined
    def test_change_org_from_hms(self):
        title = "COI Change org from hms"
        self.add_standard_team()
        self.create_request(title)
        self.submit_oar_create()
        self.assert_approvals()
        self.change_request_org("370")
        self.assert_approvals()

    @pytest.mark.dev
    @pytest.mark.combined
    def test_change_org_to_hms(self):
        title = "COI Change org to hms"
        self.add_standard_team()
        self.create_request(title, tub="370")
        self.assert_approvals()
        self.change_request_org("520")
        self.assert_approvals()

    @pytest.mark.shallow
    def test_change_pi(self):
        """
        Change the PI on HMS request
        """
        title = "COI Change request PI"
        self.create_request(title)
        self.submit_oar_create()
        self.assert_approvals()
        self.change_request_pi()
        self.assert_approvals()


if __name__ == "__main__":
    import os
    filename = os.path.basename(__file__)
    pytest.main(['%s' % filename, '-m combined'])
