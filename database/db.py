def query(db, query):
    """
    Execute a database query and return the full result set (as a tuple)
    """
    db.execute(query)
    return db.fetchall()