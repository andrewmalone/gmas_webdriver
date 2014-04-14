def create_atrisk(p):
    # from segment home...
    p = p.create_request()
    p.retro = "false"
    p.request_type = "Internal requests"
    p = p.ok()
    p.atrisk_acct = True
    p = p.ok().ok()
    p = p.edit_atrisk()
    p.checkbox = True
    p = p.ok()
    p.amount = 500
    p.start = "1/1/08"
    p.end = "1/1/08"
    p = p.ok()
    return p
