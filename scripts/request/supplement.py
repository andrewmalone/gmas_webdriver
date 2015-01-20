from selenium.common.exceptions import NoSuchElementException
import gmas_webdriver.utilities.dates as dateutil


def supplement(p, f):
    """
    Creates a supplement request (assuming start on segment home)
    """
    p = p.create_request()

    # SCR_0473
    p.request_type = "Supplement"
    p.retro = f["retro"]
    p = p.ok()

    # SCR_0089
    if "title" in f:
        p.title = f["title"]
    p.rfp = f["rfp"]
    p.subs = f["subs"]
    p.ifi = f["ifi"]
    p = p.ok()

    # SCR_0231
    p.due_date = f["due_date"]
    p.due_date_type = f["due_date_type"]
    p.copies = f["copies"]
    if "mailing" in f:
        p.mailing = f["mailing"]
    p = p.ok()

    # SCR_0090
    if "start" not in f:
        f["start"] = p.project_snapshot.start_date
    if f["start"] == "random":
        f["start"] = dateutil.random_date(p.project_snapshot.start_date, p.project_snapshot.end_date, fmt="%m-%d-%Y")

    if "end" not in f:
        f["end"] = p.project_snapshot.end_date
    if f["end"] == "random":
        f["end"] = dateutil.random_date(f["start"], p.project_snapshot.end_date, fmt="%m-%d-%Y")

    p.start = f["start"]
    p.end = f["end"]
    p = p.ok()

    # SCR_0229
    if "estimated_cost" in f:
        p.estimated_cost = f["estimated_cost"]
    p.cost_share = f["cost_share"]
    p.matching = f["matching"]
    p.on_campus = f["on_campus"]
    if p.admin_salary is not False:
        p.admin_salary = f["admin_salary"]
    p = p.ok()

    # SCR_0102
    p = p.ok()

    # subs!
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
                    p.end = f["end"]
                if "admin" in sub:
                    p.sub_admin = sub["admin"]
                if "description" in sub:
                    p.description = sub["description"]
                if "rates" in sub:
                    for i, rate in enumerate(sub["rates"]):
                        if i > 0:
                            p = p.add_rate()
                        p.rate(i + 1).rate = rate["rate"]
                        if "expiration" in rate:
                            p.rate(i + 1).expiration = rate["expiration"]
                        else:
                            # Added for random scenarios where the start/end dates of the supplement arent known
                            from datetime import datetime
                            # This format might not work in all cases
                            fmt = "%m-%d-%Y"
                            d = datetime.strptime(f["start"], fmt)
                            p.rate(i + 1).expiration = datetime.strftime(d.replace(year=d.year + (i + 1)), fmt)
                    p.basis = sub["basis"]
                p = p.ok()
        p = p.ok()

    # ifi!
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
                    p.end = f["end"]
                if "admin" in ifi:
                    p.admin = ifi["admin"]
                p = p.ok()
        p = p.ok()

    # SCR_0098 (and SCR_0365)
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
    try:
        p.human_subjects = f["human_subjects"]
    except NoSuchElementException:
        pass
    p.animals = f["animals"]
    p.biohazards = f["biohazards"]
    p.stem_cells = f["stem_cells"]
    p.protocol = f["protocol"]
    if p.foreign:
        p.foreign = f["foreign"]
    p.add_staff = f["add_staff"]
    p.use_of_name = f["use_of_name"]
    p.appt_exp = f["appt_exp"]
    if f["appt_exp"] == "true":
        p.appt_exp_option = f["appt_exp_option"]
        if f["appt_exp_option"] == "other":
            p.appt_exp_comment = f["appt_exp_comment"]
    p = p.ok()

    # SCR_0544
    if p.scr == "SCR0544":
        p.set_all_radios("false")
        p = p.ok()

    # SCR_0332
    p = p.goto_request()

    return p


if __name__ == "__main__":
    from gmas_webdriver.setup import init
    p = init("Chrome", "gdev", True)
    p = p.goto_segment(17291853)

    f = {
        # SCR_0473
        "retro": "false",
        # SCR_0089
        "title": "New supplement title",  # optional
        "rfp": "false",
        "subs": "true",
        "ifi": "true",
        # SCR_0231
        "due_date": "1/1/08",
        "due_date_type": "2401",
        "copies": "1",
        "mailing": "Mailing instructions",  # optional
        # SCR_0090
        # "start": "1/1/08",
        # "end": "12/31/08",
        # SCR_0229
        "estimated_cost": "50000",  # optional
        "cost_share": "false",
        "matching": "false",
        "admin_salary": "false",
        "on_campus": "true",
        # SCR_0091, #SCR_0092
        "subagreements": [  # optional
            {
                "name": "egg",
                "pi": "03750001"
            }
        ],
        # SCR_0228, #SCR_0094
        "ifi_list": [  # optional
            {
                "org": "31240",
                "pi": "03750001"
                # admin
            }
        ],
        # SCR_0098
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
        "protocol": "false",
        "biohazards": "false",
        "stem_cells": "false",
        "foreign": "false",
        "add_staff": "false",
        "use_of_name": "false",
        "appt_exp": "false",
        "appt_exp_option": "transfer institution",  # only required if appt_exp is true
        "appt_exp_comment": "Other"  # only required if appt_exp_option is "other"
    }

    p = supplement(p, f)
