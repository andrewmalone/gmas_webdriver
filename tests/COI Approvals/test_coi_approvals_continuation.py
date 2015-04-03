import pytest
from classes.COI_Continuation import COI_Continuation


class Test_COI_Continuation(COI_Continuation):
    @pytest.mark.tmp
    def test_continuation_basic(self):
        title = "COI Test Continuation basic"
        self.add_standard_team()
        self.create_awarded(title)
        self.assert_approvals()
        self.create_continuation()
        self.assert_approvals()

    @pytest.mark.combined
    def test_continuation_add_people(self):
        title = "COI Test Continuation combined"
        self.add_standard_team()
        self.create_awarded(title)
        self.assert_approvals()
        self.create_continuation()
        self.assert_approvals()
        self.add_standard_team_after_rgs()
        self.submit_oar_create()
        self.assert_approvals()
        self.change_all_request_flags()
        self.submit_oar_create()
        self.assert_approvals()
        self.delete_all_request_people()
        self.assert_approvals()

if __name__ == "__main__":
    # pytest.main(['-m combined', '-v', ''])
    import os
    filename = os.path.basename(__file__)
    pytest.main(['%s' % filename, '-m dev'])
