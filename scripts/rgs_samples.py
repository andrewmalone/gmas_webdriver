import copy

minimal = {
    # SCR_0088
    "org": "31570",
    "project_type": "Basic research and all other",
    "retro": "false",
    # SCR_0089
    "title": "Minimal RGS automation",
    "sponsor": "nih",
    "pi": "03750001",
    "a21": "A02-Organized Research",
    "discipline": "Arts",
    "rfp": "false",
    "subs": "false",
    "ifi": "false",
    #SCR_0231 and SCR_0231b
    "due_date": "1/1/08",
    "due_date_type": "2401",
    "copies": "1",
    # SCR_0090
    "start": "6/1/14",
    "periods": "1",
    # SCR_0229
    "cost_share": "false",
    "matching": "false",
    "admin_salary": "false",
    "program_income": "false",
    "on_campus": "true",
    # SCR_0098
    "pi_hs": "false",
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

basic_s2s = copy.deepcopy(minimal)
basic_s2s["title"] = "Minimal S2S submission (SF424 only)"
basic_s2s["opportunity"] = "NIH-UBER-4-1-2013"
basic_s2s["s2s"] = "true"
basic_s2s["ggov_questions"] = {
    "sf424_3": 2,
    "sf424_4": 2,
    "sf424_5b": "0",
    "sf424_6": 2
}

standard_s2s = copy.deepcopy(basic_s2s)
standard_s2s.update({
    "title": "Basic R01 S2S submission",
    "opportunity": "PA-C-R01",
})
standard_s2s["ggov_questions"].update({
    "rr_other_1": 2,
    "rr_other_2": 2,
    "rr_other_3": 2,
    "rr_other_4": 2,
    "ps_organization": "Harvard University",
    "ps_duns": "000000000",
    "ps_street1": "12 Oxford Street",
    "ps_city": "Cambridge",
    "ps_state": "Massachusetts",
    "ps_zip": "02138",
    "ps_country": "United States",
    "ps_district": "MA-008",
    "phs_cover_2": 1,
    "phs_cover_4": 2,
    "phs_cover_5": 2,
    "phs_cover_6": 2,
})