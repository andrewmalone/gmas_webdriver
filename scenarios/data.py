import random
import json
import os
from datetime import datetime, timedelta


def get(filename):
    with open("%s/db_data/%s.json" % (os.path.dirname(os.path.abspath(__file__)), filename), "rb") as f:
        data = json.load(f)
    return data


def random_a21():
    a21 = [
        "A02-Organized Research",
        "A03-Other Sponsored Activities",
        "A15-Scholarships & Student Aid",
        "A01-Instruction & Training"
    ]
    return random.choice(a21)


def random_discipline():
    disciplines = [
        "Astronomy",
        "Chemistry",
        "Physics",
        "Other Physical Sciences",
        "Atmospheric",
        "Earth Sciences",
        "Oceanography",
        "Other Environmental Sciences",
        "Mathematical Sciences",
        "Computer Sciences",
        "Agricultural Sciences",
        "Biological",
        "Medical (Clinical)",
        "Other Life Sciences",
        "Social Psychology",
        "Biological Psychology",
        "Economics",
        "Political Science",
        "Sociology",
        "Anthropology",
        "Education",
        "History",
        "Linguistics",
        "Geography",
        "Archaeology",
        "Urban Studies",
        "Law and Legal Studies",
        "Other Social Sciences",
        "Language & Literature",
        "Philosophy",
        "Religion",
        "Other Humanities",
        "Arts",
        "Business and Management",
        "Commun.,Journlsm,&Library Science",
        "Multi-Disciplinary",
        "Other",
        "Engineering"
    ]
    return random.choice(disciplines)


def random_orgs(n=1):
    return random.sample(get("orgs"), n)


def random_fed_sponsor(n=1):
    return random.sample(get("fed_sponsors"), n)


def random_nonfed_sponsor(n=1):
    return random.sample(get("nonfed_sponsors"), n)


def random_sponsor(n=1):
    return random.sample(get("fed_sponsors") + get("nonfed_sponsors"), n)


def random_huid(n=1):
    return random.sample(get("huids"), n)


def random_nonhuid(n=1):
    return random.sample(get("non-huids"), n)


def random_fcoi_university_policy(n=1):
    return random.sample(get("fcoi_university_policy"), n)


def random_fcoi_not_university_policy(n=1):
    all_huids = get("huids")
    fcoi_huids = get("fcoi_university_policy")
    huid_list = [p for p in all_huids if p not in fcoi_huids]
    return random.sample(huid_list, n)


def random_user(n=1):
    return random.sample(get("users"), n)


def random_active_segments(n):
    return random.sample(get("active_segments"), n)


def random_pending_segments(n):
    return random.sample(get("pending_segments"), n)


def random_closed_segments(n):
    return random.sample(get("closed_segments"), n)


def random_not_funded_segments(n):
    return random.sample(get("not_funded_segments"), n)


def person_mix(n=4):
    import math
    n = float(n)
    c = int(math.ceil(n/2))
    a = int(math.ceil((n - c)/2))
    b = int(math.floor((n - c)/2))
    p = random.sample(get("huids"), c) + random.sample(get("non-huids"), a) + random.sample(get("huids_not_in_persons"), b)
    random.shuffle(p)
    return p


def random_flag():
    return random.choice(["true", "false"])


def random_date(start="1/1/08", end="1/1/14"):
    fmt = "%m/%d/%y"
    sd = datetime.strptime(start, fmt)
    ed = datetime.strptime(end, fmt)
    dt = sd + timedelta(days=random.randint(0, (ed - sd).days))
    return datetime.strftime(dt, fmt)


def random_research_team_role(n):
    roles = get("research_team_roles")
    return [random.choice(roles) for i in range(n)]


def random_admin_team_role(n):
    roles = get("admin_team_roles")
    return [random.choice(roles) for i in range(n)]


def random_submitted_initial(n):
    return random.sample(get("submitted_initial"), n)


if __name__ == "__main__":
    fcoi_huids = get("fcoi_university_policy")
    # https://gmasdev.ca.harvard.edu/gmas/dispatch?PersonNameLinkEvent=&ref=%2Fperson%2FSCR0065PersonSearch.jsp&hUID=30628233
    # huid_list = [n for n in all_huids if n not in fcoi_huids]
    # return random.sample(huid_list, n)
    from gmas_webdriver.setup import init
    p = init("Chrome", "gdev", True)
    for huid in fcoi_huids:
        p = p.global_header.goto_people()
        p.name = huid
        p = p.search().click_first_result()
