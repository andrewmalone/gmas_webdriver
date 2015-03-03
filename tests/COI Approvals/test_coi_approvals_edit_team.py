import pytest
import common


class Test_COI_Edit(common.COI_Test):
    @pytest.mark.combined
    def test_edit_basic(self):
        """
        Test editing a confirmed team without making any changes. Should have no effect
        """
        title = "COI Test edit basic"
        self.add_standard_team()
        self.create_confirmed(title)
        self.edit_team_no_change()
        self.assert_approvals()

    @pytest.mark.combined
    def test_edit_add(self):
        """
        Test editing a confirmed team and adding the standard team
        """
        title = "COI Test edit add people"
        self.create_confirmed(title)
        self.edit_team_add_standard_team()
        self.assert_approvals()

    @pytest.mark.dev
    def test_edit_remove(self):
        title = "COI Test edit remove people"
        self.add_standard_team()
        self.create_confirmed(title)
        self.edit_team_remove_team()
        self.assert_approvals()


if __name__ == "__main__":
    import os
    filename = os.path.basename(__file__)
    pytest.main(['%s' % filename, '-m dev', '-s'])
