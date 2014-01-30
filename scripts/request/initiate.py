def initiate(p, data=None):
    # starting from 115
    p = p.initiate_review()
    page = p.get_current_page()
    if "SCR0609" in page:
        # Grants.gov form selection here
        if data != None and "forms" in data:
            for form in data["forms"]:
                p.set_form(form, data["forms"][form])  
        else:
            p.set_all_false()
        p = p.ok()

    # continue on 509

    # signatures would go here...
    p = p.ok() # to 487

    p = p.ok() # to 115
    return p
