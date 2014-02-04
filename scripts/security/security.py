from scripts.person.search import search_by_huid

def flag_user(p, huid, flag):
    """
    Flag an HUID user as Yes/No (GMAS User flag)
    Starts from: any global screen
    Ends on: SCR_0025 person profile
    """
    # First check if we are on the person profile for the correct person
    if not (p.get_current_page()[0:7] == "SCR0025" and p.huid == huid):
        # Search for the person
        p = search_by_huid(p, huid)
    if p.user_flag != flag:
        # Flag the user if the flag isn't already what we want
        p = p.edit_user()
        p.user_flag = flag
        p = p.ok()
    return p

def add_to_standing_team(p, huid, team):
    """
    Adds a user to a standing team.
    Flags the user as "Yes" if not already flagged
    Starts from: any global screen
    Ends on: SCR_0050
    """
    # Check if the person is already a user
    p = flag_user(p, huid, "Yes")
    p = p.global_header.goto_people().goto_teams()
    p.name = team
    p = p.search().row(team).go().add_member()
    p.name = huid
    p = p.search()
    p.select_first()
    p = p.ok()
    return p

def remove_from_standing_team(p, huid, team):
    """
    Remove a user from a standing team.
    Starts from: any global screen
    Ends on: SCR_0050
    """
    p = search_by_huid(p, huid)
    person_id = p.get_person_id()
    p.open_all()
    p = p.goto_standing_team(team)
    p = p.goto_member(id=person_id)
    p = p.remove_member()
    return p


