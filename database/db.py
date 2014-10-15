def query(db, query):
    """
    Execute a database query and return the full result set (as a tuple)
    """
    db.execute(query)
    return db.fetchall()


def get_list(db, q):
    """
    Execute a database query and return a list with the first column result
    """
    result = query(db, q)
    return [r[0] for r in result]


def get_single_record(db, q):
    """
    Execute a database and return the first result (one column, one row)
    """
    result = query(db, q)
    return result[0][0]

