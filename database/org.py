import db


def get_all_orgs(database):
    query = """
        select
          o.org
        from
          gmasprod.rf_orgs o
          join GMASPROD.RF_COA_SEGMENT_STATUSES status on o.COA_SEGMENT_STATUS_ID = status.COA_SEGMENT_STATUS_ID
        where
          status.description = 'Enabled'
    """
    result = db.query(database, query)
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


def get_orgs_with_tub(database):
    query = """
        select
          o.org,
          o.tub
        from
          gmasprod.rf_orgs o
          join GMASPROD.RF_COA_SEGMENT_STATUSES status on o.COA_SEGMENT_STATUS_ID = status.COA_SEGMENT_STATUS_ID
        where
          status.description = 'Enabled'
    """
    return db.query(database, query)


def get_all_orgs_for_tub(database, tub):
    query = """
        select
          o.org
        from
          gmasprod.rf_orgs o
          join GMASPROD.RF_COA_SEGMENT_STATUSES status on o.COA_SEGMENT_STATUS_ID = status.COA_SEGMENT_STATUS_ID
        where
          status.description = 'Enabled'
        and o.tub = '%s'
    """ % tub
    result = db.query(database, query)
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


def get_random_org(database, n=1, tub=None):
    import random
    if tub is None:
        orgs = get_all_orgs(database)
    else:
        orgs = get_all_orgs_for_tub(database, tub)
    return random.sample(orgs, n)
