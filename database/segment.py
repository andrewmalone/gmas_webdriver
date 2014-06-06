import db


def get_active_segments(database, created=None):
    query = """
    SELECT
        segment_id
    FROM
        segments s
        JOIN rf_segment_statuses rss ON s.segment_status_id = rss.segment_status_id
            AND rss.description = 'Active'
    """
    if created is not None:
        query += """WHERE
            s.create_date < to_date('%s','MM/DD/YYYY')
        """ % created
    return db.get_list(database, query)


def get_pending_segments(database, created=None):
    query = """
    SELECT
        segment_id
    FROM
        segments s
        JOIN rf_segment_statuses rss ON s.segment_status_id = rss.segment_status_id
            AND rss.description = 'Pending'
    """
    if created is not None:
        query += """WHERE
            s.create_date < to_date('%s','MM/DD/YYYY')
        """ % created
    return db.get_list(database, query)


def get_closed_segments(database, created=None):
    query = """
    SELECT
        segment_id
    FROM
        segments s
        JOIN rf_segment_statuses rss ON s.segment_status_id = rss.segment_status_id
            AND rss.description = 'Closed'
    """
    if created is not None:
        query += """WHERE
            s.create_date < to_date('%s','MM/DD/YYYY')
        """ % created
    return db.get_list(database, query)


def get_not_funded_segments(database, created=None):
    query = """
    SELECT
        segment_id
    FROM
        segments s
        JOIN rf_segment_statuses rss ON s.segment_status_id = rss.segment_status_id
            AND rss.description = 'Not funded'
    """
    if created is not None:
        query += """WHERE
            s.create_date < to_date('%s','MM/DD/YYYY')
        """ % created
    return db.get_list(database, query)
