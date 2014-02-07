def add_role(p, role):
    """
    Adds a role to an admin team
    Starts from: SCR_0300
    Ends on: SCR_0300
    """
    p = p.add_role()
    while not p.has_role(role):
        p = p.next()
    p.select_role(role)
    p = p.ok()
    return p