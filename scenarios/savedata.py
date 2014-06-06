import json
from gmas_webdriver.setup import init_db
import gmas_webdriver.database.org as org_query
import gmas_webdriver.database.organization as sponsor_query
import gmas_webdriver.database.person as person_query
import gmas_webdriver.database.roles as role_query
import gmas_webdriver.database.segment as segment_query
import gmas_webdriver.database.request as request_query


db = init_db("gdev")

queries = {
    # "orgs": org_query.get_all_orgs(db),
    # "fed_sponsors": sponsor_query.get_all_fed(db),
    # "nonfed_sponsors": sponsor_query.get_all_nonfed(db),
    # "huids": person_query.get_huid_persons(db),
    # "non-huids": person_query.get_nonhuid_persons(db),
    # "huids_not_in_persons": person_query.query(db, "huid_not_in_persons"),
    # "research_team_roles": role_query.get_research_team_roles(db),
    # "admin_team_roles": role_query.get_admin_team_roles(db),
    # "users": person_query.get_gmas_users(db),
    "active_segments": segment_query.get_active_segments(db, created='3/21/2014'),
    "pending_segments": segment_query.get_pending_segments(db, created='3/21/2014'),
    "closed_segments": segment_query.get_closed_segments(db, created='3/21/2014'),
    "not_funded_segments": segment_query.get_not_funded_segments(db, created='3/21/2014'),
    # "submitted_initial": request_query.get_submitted_initial(db)
}


def save(data, filename):
    with open("db_data/%s.json" % filename, "wb") as f:
        json.dump(data, f)


if __name__ == "__main__":
    for q in queries:
        save(queries[q], q)
