import db

def get_active_segment(database):
    query = """
    SELECT
        segment_id
    FROM
        segments SAMPLE(1) s
        JOIN rf_segment_statuses rss ON s.segment_status_id = rss.segment_status_id 
            AND rss.description = 'Active'
    """
    result = db.query(database, query)
    return result[0][0]