from COI_Edit import COI_Edit
from gmas_webdriver.scripts.request import continuation


class COI_Continuation(COI_Edit):
    def create_continuation(self):
        continuation_data = {
            # SCR_0472
            "retro": "false",
            # SCR_0231
            "due_date": "1/1/08",
            "due_date_type": "2401",
            "copies": "1",
            # SCR_0461
            "q1": "false",
            "q2": "false",
            "q3": "false",
            # SCR_0097
            "human_subjects": "false",
            "animals": "false",
            "biohazards": "false",
            "stem_cells": "false",
            "foreign": "false",
            "add_staff": "false",
            "use_of_name": "false",
            "appt_exp": "false",
            "cost_share": "false",
            "matching": "false",
            "admin_salary": "false",
            "protocol": "false"
        }
        self.p = continuation(self.p, continuation_data)
        self.request_id = self.p.get_id("request")
        self.request_type = "continuation"
