import db

def get_huid_not_in_persons(database):
    query = "select huid from person_searches sample(.1) where person_id is null and huid is not null"
    result = db.query(database, query)
    return result[0][0]
