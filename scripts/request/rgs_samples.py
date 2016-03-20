import copy
import datetime
import ggov_forms as forms


def add_ts(string):
    # adds a timestamp to the end of a string
    return "%s %s" % (string, datetime.datetime.now().strftime("%Y%m%d%I%M%S"))


def collect_questions(formlist):
    questions = {}
    for form, level in formlist:
        form_data = getattr(forms, form)
        if "questions" in form_data:
            if level not in form_data["questions"]:
                level = "minimal"
            if level in form_data["questions"]:
                questions.update(form_data["questions"][level])
    return questions


def collect_attachments(formlist):
    attachments = {}
    for form, level in formlist:
        form_data = getattr(forms, form)
        if "attachments" in form_data:
            if level not in form_data["attachments"]:
                level = "minimal"
            if level in form_data["attachments"]:
                attachments.update({
                    form_data["name"]: form_data["attachments"][level]
                })
    return attachments


def add_form(r, form):
    r["ggov_questions"].update(collect_questions([form]))
    r["ggov_attachments"].update(collect_attachments([form]))
    # return r


minimal = {
    # SCR_0088
    "org": "31570",
    "project_type": "Basic research and all other",
    "retro": "false",
    # SCR_0089
    "title": add_ts("Minimal RGS automation"),
    "sponsor": "egg",
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

minimal_s2s = copy.deepcopy(minimal)
minimal_s2s["title"] = add_ts("Minimal S2S submission (no data)")
minimal_s2s["opportunity"] = "NIH-UBER-4-1-2013"
minimal_s2s["s2s"] = "true"
minimal_s2s["sponsor"] = "nih"

basic_s2s = copy.deepcopy(minimal_s2s)
basic_s2s["ggov_questions"] = {
    "sf424_3": 2,
    "sf424_4": 2,
    "sf424_5b": "0",
    "sf424_6": 2
}

standard_s2s = copy.deepcopy(basic_s2s)
standard_s2s.update({
    "title": add_ts("Basic R01 S2S submission"),
    "opportunity": "PA-C-R01",
    "ggov_attachments": {
        "Research & Related Other Project Info":
            {
                "Project Summary/Abstract": "Project_Summary_Abstract.pdf",
                "Project Narrative": "Project_Narrative.pdf",
                "Bibliography & References Cited": "Bibliography.pdf"
            },
        "Research & Related Budget":
            {
                "Budget Justification": "Budget_Justification.pdf"
            },
        "Research & Related Key Person Expanded":
            {
                "Biographical Sketch": "Biosketch_PI.pdf"
            },
        "PHS398 ResearchPlan":
            {
                "Specific Aims": "Specific_Aims.pdf",
                "Research Strategy": "Research_Strategy.pdf"
            }
    }
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

s2s = {
    "empty": copy.deepcopy(minimal)
}
s2s["empty"].update({
    "title": add_ts("Minimal S2S submission (no data)"),
    "opportunity": "NIH-UBER-4-1-2013",
    "s2s": "true",
    "sponsor": "nih"
})
s2s["minimal"] = copy.deepcopy(s2s["empty"])
s2s["minimal"].update({
    "title": add_ts("Minimal S2S submission (424 only)"),
    "ggov_questions": collect_questions(forms.formlist["minimal"]),
    "ggov_attachments": collect_attachments(forms.formlist["minimal"])
})
s2s["r01_d_minimal"] = copy.deepcopy(s2s["minimal"])
s2s["r01_d_minimal"].update({
    "title": add_ts("Minimal FORMS-D R01 submission"),
    "opportunity": ("PA-DD-R01", "FORMS-D"),
    "pi": "20092297",
    "pi_credential": "eRACommons, asharpe",
    "org": "45317",
    "start": "7/1/16",
    "ggov_questions": collect_questions(forms.formlist["r01_d_minimal"]),
    "ggov_attachments": collect_attachments(forms.formlist["r01_d_minimal"])
})
s2s["r01_d_validate"] = copy.deepcopy(s2s["r01_d_minimal"])
s2s["r01_d_validate"].update({
    "title": add_ts("FORMS-D R01 NIH validated submission"),
    "ggov_questions": collect_questions(forms.formlist["r01_d_validate"]),
    "ggov_attachments": collect_attachments(forms.formlist["r01_d_validate"])
})

all_approvals = copy.deepcopy(minimal)
all_approvals.update({
    "title": add_ts("RGS All approvals"),
    "org": "16715",
    "sponsor": "bank of america",
    "prime_sponsor": "nih",
    "prime_pi": "03750002",
    "project_type": "Training grant",
    "subs": "true",
    "cost_share": "true",
    "matching": "true",
    "admin_salary": "true",
    "pi_hs": "true",
    "human_subjects": "true",
    "animals": "true",
    "biohazards": "true",
    "stem_cells": "true",
    "foreign": "true",
    "add_staff": "true",
    "use_of_name": "true",
    "appt_exp": "true",
    "appt_exp_option": "transfer institution",
    "subagreements": [
        {
            "name": "egg",
            "pi": "03750001"
        }
    ],
})

