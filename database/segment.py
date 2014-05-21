import db


def get_active_segments(database):
    query = """
    SELECT
        segment_id
    FROM
        segments s
        JOIN rf_segment_statuses rss ON s.segment_status_id = rss.segment_status_id
            AND rss.description = 'Active'
    """
    return db.get_list(database, query)
