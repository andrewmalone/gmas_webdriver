#import helpers
#d = helpers.init("Firefox", "gmastraining")
#import helpers
#d = helpers.init("Chrome", "gmasdev.cadm")


def rgs(p, f=None):
    if f is None:
        f = {
            # SCR_0088
            "org": "31570",
            "project_type": "Basic research and all other",
            "retro": "false",
            # SCR_0089
            "title": "Title",
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
            "s2s": "false",
            "due_date": "1/1/08",
            "due_date_type": "2401",
            "copies": "1",
            # SCR_0090
            "start": "1/15/08",
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
                # {
                #     "huid": "03750002",
                #     "role": "Analyst",
                #     "key": "true",
                #     "investigator": "true",
                #     "hs": "false"
                # },
                # {
                #     "huid": "03750003",
                #     "role": "Analyst",
                #     "key": "false",
                #     "investigator": "true",
                #     "hs": "false"
                # }
            ],
            # SCR_0099
            "admin_team": [
                # {
                #     "huid": "03750002",
                #     "role": "Department Administrator"
                # },
                # {
                #     "huid": "03750003",
                #     "role": "Central Administrator"
                # }
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

    #from pages.SCR0270 import SCR0270
    #p = SCR0270(d).nav_to()
    p = p.create_proposal()

    # SCR_0088
    p.org = f["org"]
    p.project_type = f["project_type"]
    p.retro = f["retro"]
    p = p.ok()

    # SCR_0089
    p.title = f["title"]
    p.sponsor = f["sponsor"]
    p.pi = f["pi"]
    if f["prime_sponsor"] != "":
        p.prime_sponsor = f["prime_sponsor"]
        p.prime_pi = f["prime_pi"]
    p.a21 = f["a21"]
    p.discipline = f["discipline"]
    p.rfp = f["rfp"]
    p.subs = f["subs"]
    p.ifi = f["ifi"]
    p = p.ok()

    # Need to check for which screen... (231 or 613)
    if p.get_current_page() == "SCR0613EnterOpportunity":
        if f["opportunity"] != "":
            p.opportunity = f["opportunity"]
        p = p.ok()

    # SCR_0231 or SCR_0231b
    p.due_date = f["due_date"]
    if p.get_current_page() == "SCR0231bRequestSubmissionDetails":
        p.s2s = f["s2s"]
    if p.get_current_page() == "SCR0231RequestSubmissionDetails" or f["s2s"] == "false":
        p.due_date_type = f["due_date_type"]
        p.copies = f["copies"]
    p = p.ok()

    # SCR_0090
    p.start = f["start"]
    p.calc_end(f["start"], f["periods"])
    p.periods = f["periods"]
    p = p.ok()

    # SCR_0227
    p.calc_periods(f["start"], f["periods"])
    p = p.ok()

    # SCR_0229
    p.cost_share = f["cost_share"]
    p.matching = f["matching"]
    p.program_income = f["program_income"]
    p.on_campus = f["on_campus"]
    if p.admin_salary is True:
        p.admin_salary = f["admin_salary"]
    p = p.ok()

    # SCR_0102
    p = p.ok()

    # SUBS and IFI get added here...

    # SCR_0098 (and SCR_0365)
    p = p.edit_pi()
    p.human_subjects = f["pi_hs"]
    p = p.ok()
    for person in f["research team"]:
        p = p.add_member()
        p.role = person["role"]
        p.lookup_person(person["huid"])
        p.key = person["key"]
        p.human_subjects = person["hs"]
        if person["key"] == "false" and p.investigator is True:
            p.investigator = person["investigator"]
        p = p.ok()

    p = p.ok()

    # SCR_0099
    if "admin_team" in f:
        for person in f["admin_team"]:
            p = p.add_member()
            # SCR_0230
            p.role = person["role"]
            p.name = person["huid"]
            p = p.ok()
    p = p.ok()

    # SCR_0097
    p.human_subjects = f["human_subjects"]
    p.animals = f["animals"]
    p.biohazards = f["biohazards"]
    p.stem_cells = f["stem_cells"]
    if p.foreign:
        p.foreign = f["foreign"]
    p.add_staff = f["add_staff"]
    p.use_of_name = f["use_of_name"]
    p.appt_exp = f["appt_exp"]
    p = p.ok()

    # SCR_0544
    p.set_all_radios("false")
    p = p.ok()

    # S2S screens go here...
    if f["s2s"] == "true":
        # SCR_0612b
        p = p.ok()
        # SCR_0610b
        p = p.ok()

    # SCR_0332
    p = p.go_req()
    return p
