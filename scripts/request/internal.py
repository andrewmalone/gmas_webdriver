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


def create_admin(p, f={}):
    """
    Starts from a segment home and creates a changes to existing segment request
    {
        "preaward": True,
        "carryforward": False,
        "nocost": False,
        "equipment": False,
        "sub": False,
        "ifi": False,
        "changepi": False,
        "rebudget": False,
        "termination": False,
    }
    """
    if p.scr != "SCR0104":
        raise Exception("Not on segment home")

    p = p.create_request()

    # SCR_0472
    p.request_type = "Changes to existing segment"
    p.retro = f["retro"] if "retro" in f else "false"
    p = p.ok()

    # SCR_0541
    p.preaward = f["preaward"] if "preaward" in f else False
    p.carryforward = f["carryforward"] if "carryforward" in f else False
    p.nocost = f["nocost"] if "nocost" in f else False
    p.equipment = f["equipment"] if "equipment" in f else False
    p.sub = f["sub"] if "sub" in f else False
    p.ifi = f["ifi"] if "ifi" in f else False
    p.changepi = f["changepi"] if "changepi" in f else False
    p.rebudget = f["rebudget"] if "rebudget" in f else False
    p.termination = f["termination"] if "termination" in f else False
    p = p.ok()

    # SCR_0465
    if "justification" in f:
        p.justification = f["justification"]
    p = p.ok()

    return p
