import pytest
from classes.COI_Edit import COI_Edit


class Test_COI_Edit(COI_Edit):
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

    @pytest.mark.combined
    @pytest.mark.parametrize('oar', [True, False])
    def test_edit_remove(self, oar):
        """
        Test editing a confirmed team - deleting all people
        """
        title = "COI Test edit remove people"
        self.add_standard_team()
        self.create_confirmed(title, submit_oar=oar)
        self.edit_team_remove_team()
        self.assert_approvals()

    @pytest.mark.combined
    @pytest.mark.parametrize('oar', [True, False])
    def test_edit_add_then_remove(self, oar):
        title = "COI Test edit add and remove"
        self.create_confirmed(title)
        self.edit_team_add_standard_team()
        if oar:
            self.submit_oar_create()
        self.assert_approvals()
        self.edit_team_remove_team()
        self.assert_approvals()

    @pytest.mark.combined
    @pytest.mark.parametrize('oar', [True, False])
    def test_edit_change_flags(self, oar):
        title = "COI Test edit change flags"
        self.add_standard_team()
        self.create_confirmed(title)
        self.edit_team_add_standard_team()
        if oar:
            self.submit_oar_create()
        self.assert_approvals()
        self.edit_team_change_flags()
        self.assert_approvals()


if __name__ == "__main__":
    import os
    filename = os.path.basename(__file__)
    pytest.main(['%s' % filename, '-m combined', '-v'])
