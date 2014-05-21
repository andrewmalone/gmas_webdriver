from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException


def continuation(p, f):
    """
    Creates a continuation request (assuming start on segment home)
    """
    p = p.create_request()

    # SCR_0472
    p.request_type = "Continuation"
    p.retro = f["retro"]
    p = p.ok()

    # SCR_0512
    # any edits to dates would go here...
    if p.end == "":
        fmt = "%m-%d-%Y"
        d = datetime.strptime(p.start, fmt)
        d = d.replace(year=d.year+1) + timedelta(days=-1)
        p.end = datetime.strftime(d, fmt)
    p = p.ok()

    # SCR_0231
    p.due_date = f["due_date"]
    p.due_date_type = f["due_date_type"]
    p.copies = f["copies"]
    if "mailing" in f:
        p.mailing = f["mailing"]
    p = p.ok()

    # SCR_0461 (maybe!)
    if p.scr == "SCR0461":
        p.q1 = f["q1"]
        p.q2 = f["q2"]
        p.q3 = f["q3"]
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
    p.cost_share = f["cost_share"]
    p.matching = f["matching"]
    if p.admin_salary is True:
        p.admin_salary = f["admin_salary"]
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
    p = init("Chrome", "gdev")
    p = p.goto_segment(15863433)

    f = {
        # SCR_0472
        "retro": "false",
        # SCR_0231
        "due_date": "1/1/08",
        "due_date_type": "2401",
        "copies": "1",
        "mailing": "Mailing instructions",  # optional
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
        "appt_exp_option": "transfer institution",  # only required if appt_exp is true
        "attp_exp_comment": "Other",  # only required if appt_exp_option is "other"
        "cost_share": "false",
        "matching": "false",
        "admin_salary": "false",
        "protocol": "false"
    }

    p = continuation(p, f)
