import db


def get_submitted_initial(database):
    query = """
    select
      r.segment_id,
      r.request_id
    from
      gmasprod.requests r
      join gmasprod.rf_request_statuses rs on r.request_status_id = rs.request_status_id
      join gmasprod.rf_request_types rt on r.request_type_id = rt.request_type_id
      join gmasprod.segments s on r.segment_id = s.segment_id
    where
      rt.description in  ('Initial request', 'Competing renewal')
      and rs.description = 'Submitted to sponsor'
      and r.create_date < to_date('3/21/2014','MM/DD/YYYY')
    order by
      r.create_date desc
    """
    return db.query(database, query)
