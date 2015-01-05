def confirm_team(p):
    if p.scr != "SCR0104b":
        p = p.project_snapshot.goto_segment_home()

    p = p.confirm_research_team()
    count = p.person_count
    for i in range(count):
        person = p.person(i + 1)
        person.cal_effort = "10"
        if i > 0:
            person.sponsor_commitment = "No"
    p = p.ok()

    return p
