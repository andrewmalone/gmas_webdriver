import copy
import random
from gmas_webdriver.scripts.request.rgs import samples
import data


def add_scenario(scenarios, update):
    f = copy.deepcopy(samples.minimal)
    f.update(update)
    scenarios.append(f)


def rand_baseline(n=1):
    """
    Create a randomized baseline rgs scenario based on the minimal data
    """
    orgs = data.random_orgs(n)
    sponsors = data.random_sponsor(n)
    pis = data.random_huid(n)
    scenarios = []
    for i in range(n):
        f = {
            # SCR_0088
            "org": orgs[i],
            "project_type": random.choice(["Basic research and all other", "Task order", "Training grant"]),
            "retro": data.random_flag(),
            # SCR_0089
            "title": samples.add_ts("Minimal RGS automation"),
            "sponsor": sponsors[i],
            "pi": pis[i],
            "a21": data.random_a21(),
            "discipline": data.random_discipline(),
            "rfp": data.random_flag(),
            "subs": "false",
            "ifi": "false",
            #SCR_0231 and SCR_0231b
            "due_date": data.random_date(),
            "due_date_type": random.choice(["2401", "2402"]),
            "copies": str(random.randint(1, 10)),
            # SCR_0090
            "start": data.random_date(),
            "periods": str(random.randint(1, 5)),
            # SCR_0229
            "cost_share": "false",
            "matching": "false",
            "admin_salary": "false",
            "program_income": "false",
            "on_campus": data.random_flag(),
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
        scenarios.append(f)
    return scenarios


def s1(n=20):
    """
    n projects:
        * uses random baseline
        * half random nonfed sponsors, half random fed sponsors
    """
    scenarios = rand_baseline(n)
    sponsors = data.random_fed_sponsor(n/2) + data.random_nonfed_sponsor(n/2)
    pis = data.person_mix(n)
    for i, scenario in enumerate(scenarios):
        scenario.update({
            "title": samples.add_ts("RGS S1 %s" % (i + 1)),
            "pi": pis[i],
            "sponsor": sponsors[i]
        })
    return scenarios


def s2(n=20):
    """
    Same as S1, but using Fellowship (Random Mentor with HUID)
    """
    scenarios = s1(n)
    mentors = data.person_mix(n)
    for i, scenario in enumerate(scenarios):
        # add mentor, fellowship
        scenario.update({
            "title": samples.add_ts("RGS S2 %s" % (i + 1)),
            "project_type": "Fellowship",
            "mentor": mentors[i],
            "mentor_hs": "false",
            "mentor_key": "true"
        })
    return scenarios


def s3(n=2):
    """
    Prime sponsor (not Fellowship)
    1/2 projects with non-fed direct + fed prime
    1/2 projects with non-fed direct + non-fed prime
    """
    scenarios = s1(n)
    sponsors = data.random_nonfed_sponsor(n)
    prime_sponsors = data.random_fed_sponsor(n/2) + data.random_nonfed_sponsor(n/2)
    prime_pis = data.person_mix(n)
    for i, scenario in enumerate(scenarios):
        scenario.update({
            "title": samples.add_ts("RGS S3 %s" % (i + 1)),
            "prime_pi": prime_pis[i],
            "prime_sponsor": prime_sponsors[i],
            "sponsor": sponsors[i]
            })
    return scenarios


def s4(n=2):
    """
    Subagreements (basic)
    """
    num_subs = n
    scenarios = rand_baseline(1)
    sub_orgs = data.random_nonfed_sponsor(num_subs)
    sub_pis = data.random_huid(num_subs)
    for i, scenario in enumerate(scenarios):
        scenario.update({
            "title": samples.add_ts("RGS S4 sub basic"),
            "subs": "true",
            "subagreements": []
            })
        for j in range(num_subs):
            scenario["subagreements"].append({
                "name": sub_orgs[j],
                "pi": sub_pis[j]
                })
    return scenarios


def s5(n=1):
    """
    IFI (basic) (n = number of ifi to add)
    """
    scenarios = rand_baseline(1)
    ifi_orgs = data.random_orgs(n)
    ifi_pis = data.random_huid(n)
    ifi_admins = data.random_user(n)
    ifi_list = []
    for i in range(n):
        ifi_list.append({
            "org": "45310",  # ifi_orgs[i],
            "pi": "60157898"  # ifi_pis[i]
            #"admin": ifi_admins[i]
            })
    scenarios[0].update({
        "title": samples.add_ts("RGS S5 IFI basic"),
        "ifi": "true",
        "ifi_list": ifi_list
        })
    return scenarios


def s6(n=1, other=None, tbd=None, scenarios=None):
    """
    Research team variations (n = number of research team to add)
    """
    if scenarios is None:
        scenarios = rand_baseline(1)
    for num, scenario in enumerate(scenarios):
        members = data.person_mix(n)
        roles = data.random_research_team_role(n)
        team = []
        for i in range(n):
            team.append({
                "huid": members[i],
                "role": roles[i],
                "key": random.choice(["true", "false"]),
                "investigator": random.choice(["true", "false"]),
                "hs": random.choice(["true", "false"])
                })
        if other is not None:
            # make the last role an "other"
            team[-1].update({
                "role": "Other",
                "other_role_description": other
                })
        if tbd is not None:
            # make some roles TBD
            for i in range(tbd):
                team[i].update({
                    "huid": "tbd",
                    "key": "false"
                    })
        scenario.update({
            "title": samples.add_ts("RGS S6.%i Research team" % (num + 1)),
            "research team": team,
            "human_subjects": "true"
            })
    return scenarios


def s7(n=1):
    """
    Admin team (n = number of people to add)
    """
    scenarios = rand_baseline(1)
    admin_people = data.random_user(n)
    admin_roles = data.random_admin_team_role(n)
    admin_list = []
    for i in range(n):
        admin_list.append({
            "huid": admin_people[i],
            "role": admin_roles[i]
            })
    scenarios[0].update({
        "title": samples.add_ts("RGS S7 Admin team"),
        "admin_team": admin_list
        })
    return scenarios


def s8(n=1, scenarios=None):
    """
    Subagreements (extended)
    """
    from datetime import datetime
    if scenarios is None:
        scenarios = rand_baseline(1)
    for num, scenario in enumerate(scenarios):
        sub_orgs = data.random_nonfed_sponsor(n)
        sub_pis = data.person_mix(n)
        sub_admins = data.person_mix(n)
        sub_list = []
        for i in range(n):
            sub = {}
            num_rates = random.randint(0, 2)
            if num_rates > 0:
                sub["rates"] = []
            for r in range(num_rates):
                fmt = "%m/%d/%y"
                d = datetime.strptime(scenario["start"], fmt)
                ed = datetime.strftime(d.replace(year=d.year + (r + 1)), fmt)
                sub["rates"].append({
                    "rate": "%s" % random.randint(10, 60),
                    "expiration": ed
                    })
            sub.update({
                "admin": sub_admins[i],
                "description": "Sub description %s" % (i + 1),
                "basis": "Total Direct Costs",
                "pi": sub_pis[i],
                "name": sub_orgs[i]
                })
            sub_list.append(sub)
        scenario.update({
            "title": samples.add_ts("RGS S8.%i Subs" % (num + 1)),
            "subs": "true",
            "subagreements": sub_list
            })
    return scenarios


def s9():
    """
    S2S
    """
    scenarios = rand_baseline(1)
    orgs = data.random_fed_sponsor(1)
    for i, scenario in enumerate(scenarios):
        scenario.update({
            "sponsor": orgs[i],
            "s2s": "true",
            "opportunity": "PA-C-R01"
            })
    return scenarios


def s10():
    return [samples.standard_s2s]


def all_approvals():
    scenarios = []
    scenarios.append(samples.all_approvals)
    return scenarios


if __name__ == "__main__":
    print [s["subagreements"] for s in s8(2, scenarios=s1(4))]
