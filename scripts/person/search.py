def search_by_huid(p, huid):
    p = p.global_header.goto_people()
    p.name = huid
    p = p.search()
    p = p.click_first_result()
    return p