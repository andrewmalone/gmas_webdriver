import os
import rgs_samples as samples


def calc_end(start_date, num_periods):
    """
    helper method - sets the end date field based on the start date and the number of periods (assumes 1 year period)
    example: calc_end("6/1/08", 2) would set the end date to 5/30/10
    """
    from datetime import datetime, date, timedelta
    start = datetime.strptime(start_date, "%m/%d/%y")
    end = date.strftime(date(start.year + int(num_periods), start.month, start.day) - timedelta(days=1), "%m/%d/%y")
    return end


def checkstop(p, stop):
    if stop is None:
        return False
    if p.scr == stop:
        return True
    else:
        return False


def rgs(p, f=None, finish="request", stop=None):
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
            # optional
            "mentor": "",
            # optional
            "prime_sponsor": "",
            # optional
            "prime_pi": "",
            "a21": "A02-Organized Research",
            "discipline": "Arts",
            "rfp": "false",
            "subs": "false",
            "ifi": "false",
            # SCR_0613
            "opportunity": "PA-C-R01",  # optional
            #SCR_0231 and SCR_0231b
            "s2s": "true",  # optional
            "due_date": "1/1/08",
            "due_date_type": "2401",
            "copies": "1",
            "mailing": "Mailing instructions",  # optional
            # SCR_0090
            "start": "1/15/08",
            "periods": "4",
            # SCR_0229
            "estimated_cost": "50000",  # optional
            "cost_share": "false",
            "matching": "false",
            "admin_salary": "false",
            "program_income": "false",
            "on_campus": "true",
            # SCR_0102
            "template": "nih",  # optional
            # SCR_0091, #SCR_0092
            "subagreements": [  # optional
                {
                    "name": "egg",
                    "pi": "03750001"
                },
                {
                    "name": "lincoln",
                    "pi": "03750002",
                    "start": "2/15/08",  # optional
                    "end": "3/15/08"  # optional
                    # add rate detail here!
                }
            ],
            # SCR_0228, #SCR_0094
            "ifi_list": [  # optional
                {
                    "org": "31240",
                    "pi": "03750001"
                    # admin
                },
                {
                    "org": "31570",
                    "pi": "03750003",
                    "start": "2/15/08",  # optional
                    "end": "3/15/08"  # optional
                }
            ],
            # SCR_0098
            "pi_hs": "false",
            "mentor_hs": "false",  # optional (required if fellowship)
            "mentor_key": "false",  # optional (required  if fellowship)
            "research team": [  # optional
                {
                    "huid": "03750002",  # can be tbd
                    "role": "Analyst",
                    "key": "true",
                    "investigator": "true",
                    "hs": "false"
                },
                {
                    "huid": "03750003",
                    "role": "Other",
                    "other_role_description": "school bus driver",
                    "key": "false",
                    "investigator": "true",
                    "hs": "false"
                }
            ],
            # SCR_0099
            "admin_team": [  # optional
                {
                    "huid": "03750002",
                    "role": "Department Administrator"
                },
                {
                    "huid": "03750003",
                    "role": "Central Administrator"
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
            "appt_exp": "false",
            "appt_exp_option": "transfer institution",  # only required if appt_exp is true
            "appt_exp_comment": "Other",  # only required if appt_exp_option is "other"
            # SCR_0612b
            "ggov_questions": {  # optional
                "sf424_3": 2,
                "sf424_4": 1,
                "sf424_4a": "Other agency",
                "sf424_5b": "0",
                "sf424_6": 2
            },
            "ggov_attachments": {
                "directory": "%s\\s2s\\" % os.path.dirname(os.path.abspath(__file__)),
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
        }

    p = p.create_proposal()

    # SCR_0088
    p.org = f["org"]
    p.project_type = f["project_type"]
    p.retro = f["retro"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0089
    p.title = f["title"]
    p.sponsor = f["sponsor"]
    p.pi = f["pi"]
    if "mentor" in f and f["mentor"] != "" and f["project_type"] == "Fellowship":
        p.mentor = f["mentor"]
    if "prime_sponsor" in f and f["prime_sponsor"] != "":
        p.prime_sponsor = f["prime_sponsor"]
        p.prime_pi = f["prime_pi"]
    p.a21 = f["a21"]
    p.discipline = f["discipline"]
    p.rfp = f["rfp"]
    p.subs = f["subs"]
    p.ifi = f["ifi"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # Need to check for which screen... (231 or 613)
    if p.get_current_page() == "SCR0613EnterOpportunity":
        if "opportunity" in f and f["opportunity"] != "":
            p.opportunity = f["opportunity"]
        if checkstop(p, stop):
            return p
        p = p.ok()

    # SCR_0231 or SCR_0231b
    p.due_date = f["due_date"]
    if "s2s" not in f:
        f["s2s"] = "false"
    if p.get_current_page() == "SCR0231bRequestSubmissionDetails":
        p.s2s = f["s2s"]
    if p.get_current_page() == "SCR0231RequestSubmissionDetails" or f["s2s"] == "false":
        p.due_date_type = f["due_date_type"]
        p.copies = f["copies"]
        if "mailing" in f:
            p.mailing = f["mailing"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0090
    p.start = f["start"]
    p.calc_end(f["start"], f["periods"])
    p.periods = f["periods"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0227
    p.calc_periods(f["start"], f["periods"])
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0229
    if "estimated_cost" in f:
        p.estimated_cost = f["estimated_cost"]
    p.cost_share = f["cost_share"]
    p.matching = f["matching"]
    p.program_income = f["program_income"]
    p.on_campus = f["on_campus"]
    if p.admin_salary is not False:
        p.admin_salary = f["admin_salary"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0102
    if "template" in f:
        p.template = f["template"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SUBS and IFI get added here...
    # SCR_0091
    if f["subs"] == "true":
        if "subagreements" in f:
            for sub in f["subagreements"]:
                p = p.add_sub()
                # SCR_0092
                p.sub_name = sub["name"]
                p.sub_pi = sub["pi"]
                if "start" in sub and "end" in sub:
                    p.start = sub["start"]
                    p.end = sub["end"]
                else:
                    p.start = f["start"]
                    p.end = calc_end(f["start"], f["periods"])
                if "admin" in sub:
                    p.sub_admin = sub["admin"]
                if "description" in sub:
                    p.description = sub["description"]
                if "rates" in sub:
                    for i, rate in enumerate(sub["rates"]):
                        if i > 0:
                            p = p.add_rate()
                        p.rate(i + 1).rate = rate["rate"]
                        p.rate(i + 1).expiration = rate["expiration"]
                    p.basis = sub["basis"]
                p = p.ok()
        if checkstop(p, stop):
            return p
        p = p.ok()

    # SCR_0228
    if f["ifi"] == "true":
        if "ifi_list" in f:
            for ifi in f["ifi_list"]:
                p = p.add_ifi()
                # SCR_0094
                p.org = ifi["org"]
                p.pi = ifi["pi"]
                if "start" in ifi and "end" in ifi:
                    p.start = ifi["start"]
                    p.end = ifi["end"]
                else:
                    p.start = f["start"]
                    p.end = calc_end(f["start"], f["periods"])
                if "admin" in ifi:
                    p.admin = ifi["admin"]
                p = p.ok()
        if checkstop(p, stop):
            return p
        p = p.ok()

    # SCR_0098 (and SCR_0365)
    p = p.edit_pi()
    p.human_subjects = f["pi_hs"]
    p = p.ok()
    if f["project_type"] == "Fellowship":
        p = p.edit_mentor()
        p.human_subjects = f["mentor_hs"]
        p.key = f["mentor_key"]
        if f["mentor_key"] == "false" and p.investigator is not False:
            p.investigator = f["mentor_investigator"]
        p = p.ok()
    if "research team" in f:
        for person in f["research team"]:
            p = p.add_member()
            p.role = person["role"]
            if person["role"] == "Other":
                p.other_role_description = person["other_role_description"]
            if person["huid"] == "tbd":
                p.tbd = True
            else:
                p.person = person["huid"]
            p.key = person["key"]
            p.human_subjects = person["hs"]
            if p.investigator is not False:
                p.investigator = person["investigator"]
            p = p.ok()
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0099
    if "admin_team" in f:
        for person in f["admin_team"]:
            p = p.add_member()
            # SCR_0230
            p.role = person["role"]
            p.name = person["huid"]
            p = p.ok()
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0097
    p.human_subjects = f["human_subjects"]
    p.animals = f["animals"]
    p.biohazards = f["biohazards"]
    p.stem_cells = f["stem_cells"]
    if p.foreign is not False:
        p.foreign = f["foreign"]
    p.add_staff = f["add_staff"]
    p.use_of_name = f["use_of_name"]
    p.appt_exp = f["appt_exp"]
    if f["appt_exp"] == "true":
        p.appt_exp_option = f["appt_exp_option"]
        if f["appt_exp_option"] == "other":
            p.appt_exp_comment = f["appt_exp_comment"]
    if checkstop(p, stop):
        return p
    p = p.ok()

    # SCR_0544
    if p.scr == "SCR0544":
        p.set_all_radios("false")
        if checkstop(p, stop):
            return p
        p = p.ok()

    # S2S screens go here...
    if f["s2s"] == "true":
        # SCR_0612b
        if "ggov_questions" in f:
            # @todo - add support for multiple performance sites
            for question in sorted(f["ggov_questions"].keys()):
                setattr(p, question, f["ggov_questions"][question])
        if checkstop(p, stop):
            return p
        p = p.ok()

        # SCR_0610b
        if "ggov_attachments" in f:
            if "directory" in f["ggov_attachments"]:
                base_dir = f["ggov_attachments"]["directory"]
            else:
                # base_dir = "%s\\s2s_attachments\\" % os.path.dirname(os.path.abspath(__file__))
                base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s2s_attachments")
            for form in f["ggov_attachments"]:
                if form == "directory":
                    continue
                for attachment in f["ggov_attachments"][form]:
                    p = p.locate(form, attachment)
                    p.set_file(os.path.join(base_dir, f["ggov_attachments"][form][attachment]))
                    # print "%s%s" % (base_dir, f["ggov_attachments"][form][attachment])
                    p = p.ok()
        if checkstop(p, stop):
            return p
        p = p.ok()

    # SCR_0332
    if checkstop(p, stop):
        return p
    if finish == "budget":
        p = p.goto_budget()
    else:
        p = p.goto_request()

    return p

if __name__ == "__main__":
    from gmas_webdriver.setup import init
    p = init("Chrome", "gdev", False)
    #p = rgs(p)
