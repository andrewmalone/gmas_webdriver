def r2r(p):
    # start from the request home
    p = p.r2r()
    # 409
    p = p.ok()
    # 402b (or a?)
    p.due_date = "1/1/08"
    p.due_date_type = "receipt"
    p.copies = "1"
    p = p.ok()
    return p
