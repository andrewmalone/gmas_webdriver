import db
import random


queries = {
    "huid_not_in_persons": """
        select huid from gmasprod.person_searches sample where person_id is null and huid is not null
        """,
    "huid": """
        select huid from gmasprod.persons where huid is not null
        """,
    "non-huid": """
        select first_name || ' ' || last_name from gmasprod.persons where huid is null
        """,
    "users": """
        select huid from gmasprod.persons where valid_user_flag = 1 and disabled_flag = 0
        """
}


def query(database, query):
    result = db.query(database, queries[query])
    for i in range(len(result)):
            result[i] = result[i][0]
    return result


def get_huid_persons(database):
    return query(database, "huid")


def get_nonhuid_persons(database):
    return query(database, "non-huid")


def get_huid_not_in_persons(database, n=1):
    return random.sample(query(database, "huid_not_in_persons"), n)


def get_huid(database, n=1):
    return random.sample(query(database, "huid"), n)


def get_non_huid(database, n=1):
    return random.sample(query(database, "non-huid"), n)


def get_gmas_users(database):
    return query(database, "users")
