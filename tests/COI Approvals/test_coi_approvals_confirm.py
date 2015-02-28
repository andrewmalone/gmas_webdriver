import pytest
import common


class Test_COI_Confirm(common.COI_Test):
    @pytest.mark.combined
    def test_confirm_basic(self):
        """
        Confirm with standard team
        No changes when confirming the team
        """
        title = "COI confirm team basic"
        self.add_standard_team()
        self.create_request(title)
        self.assert_approvals()
        self.confirm_team()
        self.assert_approvals()

    @pytest.mark.combined
    def test_confirm_add_team(self):
        """
        Add standard team at confirm
        """
        title = "COI confirm team add people"
        self.create_to_confirm(title)
        self.add_standard_team_at_confirm()
        self.confirm_team()
        self.assert_approvals()

    @pytest.mark.combined
    @pytest.mark.parametrize('oar', [True, False])
    def test_confirm_remove_team(self, oar):
        title = "COI confirm team delete people"
        self.add_standard_team()
        self.create_to_confirm(title, submit_oar=oar)
        self.delete_team_at_confirm()
        self.confirm_team()
        self.assert_approvals()

    @pytest.mark.combined
    @pytest.mark.parametrize('oar', [True, False])
    def test_confirm_change_flags(self, oar):
        title = "COI confirm team change flags"
        self.add_standard_team()
        self.create_to_confirm(title, submit_oar=oar)
        self.change_confirm_flags()
        self.confirm_team()
        self.assert_approvals()

if __name__ == "__main__":
    # pytest.main(['-m combined', '-v', ''])
    import os
    filename = os.path.basename(__file__)
    pytest.main(['%s' % filename, '-m combined', '-s'])
