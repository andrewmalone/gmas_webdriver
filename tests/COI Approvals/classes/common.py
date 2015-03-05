from gmas_webdriver.scenarios import data
from gmas_webdriver.scripts.request import samples

standard_team = [
        {
            "key": "true",
            "investigator": "true",
            "university": "1"
        },
        {
            "key": "true",
            "investigator": "true",
            "university": "0"
        },
        {
            "key": "true",
            "investigator": "false",
            "university": "1"
        },
        {
            "key": "true",
            "investigator": "false",
            "university": "0"
        },
        {
            "key": "false",
            "investigator": "true",
            "university": "1"
        },
        {
            "key": "false",
            "investigator": "true",
            "university": "0"
        },
        {
            "key": "false",
            "investigator": "false",
            "university": "1"
        },
        {
            "key": "false",
            "investigator": "false",
            "university": "0"
        }
    ]


def req_with_team(pi, team, title, org="31240", sponsor="nih"):
    """
    Returns an rgs object with the specified research team
    pi: HUID string
    team: research team data object
    """
    req = samples.minimal
    req["pi"] = pi
    req["org"] = org
    req["sponsor"] = sponsor
    req["research team"] = team
    req["title"] = samples.add_ts(title)
    return req


def research_team_record(key, investigator, university=None):
    """
    Returns a research team dictionary for use in an rgs data object
    key and investigator should be "true" or "false"
    """
    person = data.random_huid_with_name(university=university)

    team_member = {
        "huid": person[0],
        "name": person[1],
        "role": data.random_research_team_role(),
        "hs": "false",
        "key": key,
        "investigator": investigator,
        "university": person[2]
    }
    return team_member


def map_value(value):
    if value == "true":
        return "Yes"
    elif value == "false":
        return "No"
    return value
