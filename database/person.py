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
        """,
    "fcoi_university_policy": """
        select
          huid
        from
          gmasprod.coi
        where
          university_policy = 1
      """,
    "huid_with_name": """
        select huid, last_name || ', ' || first_name from gmasprod.persons where huid is not null
        """,
    "huid_with_data": """
        select
          p.huid,
          p.last_name || ', ' || p.first_name,
          nvl(coi.university_policy, 'null') as university_policy
        from
          persons p
          left join gmasprod.coi coi on p.huid = coi.huid
        where
          p.huid is not null
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


def get_fcoi_university_policy(database):
    return query(database, "fcoi_university_policy")


def get_huids_with_names(database):
    return db.query(database, queries["huid_with_name"])


def get_huids_with_data(database):
    return db.query(database, queries["huid_with_data"])
