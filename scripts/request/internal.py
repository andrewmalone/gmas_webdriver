def create_internal(p, f={}):
    """
    Starts from a segment home and creates an internal or changes to existing request
    Segment must be active!
    {
        "atrisk": True,
        "change_tub": True,
        "new_acct": True
    }
    """
    if p.scr != "SCR0104":
        raise Exception("Not on segment home")

    # todo - check for segment status, check for correct format of f

    p = p.create_request()

    # SCR_0472
    p.request_type = "Internal requests"
    p.retro = f["retro"] if "retro" in f else "false"
    p = p.ok()

    # SCR_0542
    p.atrisk_acct = f["atrisk"]
    p.change_tub = f["change_tub"]
    p.new_acct = f["new_acct"]
    p = p.ok()

    # SCR_0465
    if "justification" in f:
        p.justification = f["justification"]
    p = p.ok()

    return p

