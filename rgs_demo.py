import scripts.setup as setup
from scripts.rgs import rgs

f = {
    # SCR_0088
    "org": "31570",
    "project_type": "Basic research and all other",
    "retro": "false",
    # SCR_0089
    "title": "Basic request for testing SCR_0650 (2)",
    "sponsor": "nih",
    "pi": "03750001",
    "prime_sponsor": "",
    "prime_pi": "",
    "a21": "A02-Organized Research",
    "discipline": "Arts",
    "rfp": "false",
    "subs": "false",
    "ifi": "false",
    # SCR_0613
    "opportunity": "",
    #SCR_0231 and SCR_0231b
    "s2s": "",
    "due_date": "1/1/08",
    "due_date_type": "2401",
    "copies": "1",
    # SCR_0090
    "start": "8/1/13",
    "periods": "1",
    # SCR_0229
    "cost_share": "false",
    "matching": "false",
    "admin_salary": "false",
    "program_income": "false",
    "on_campus": "true",
    # SCR_0098
    "pi_hs": "false",
    "research team": [
    {
        "huid": "03750010",
        "role": "Analyst",
        "key": "true",
        "investigator": "true",
        "hs": "false"
    }
    ],
    # SCR_0097
    "human_subjects": "false",
    "animals": "false",
    "biohazards": "false",
    "stem_cells": "false",
    "foreign": "false",
    "add_staff": "false",
    "use_of_name": "false",
    "appt_exp": "false"
}

p = setup.init("Firefox", "gmasdev.cadm")
p = rgs(p, f)

