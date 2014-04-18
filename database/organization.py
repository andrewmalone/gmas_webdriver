import db
import random

queries = {
    "all_fed": """
        select
          full_name
        from
          gmasprod.organizations
        where
          us_federal_org_flag = 1
        """,
    "all_nonfed": """
        select
          full_name
        from
          gmasprod.organizations
        where
          us_federal_org_flag = 0
        """,
    "all": """
        select full_name
        from gmasprod.organizations
        """
}


def query(database, query):
    result = db.query(database, queries[query])
    for i in range(len(result)):
            result[i] = result[i][0]
    return result


def get_all_fed(database):
    return query(database, "all_fed")


def get_all_nonfed(database):
    return query(database, "all_nonfed")


def get_random_fed(database, n=1):
    return random.sample(query(database, "all_fed"), n)


def get_random_nonfed(database, n=1):
    return random.sample(query(database, "all_nonfed"), n)
