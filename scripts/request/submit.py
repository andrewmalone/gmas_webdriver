def submit(p):
    pass

def submit_s2s(p, data=None):
    # start from request home
    p = p.prepare_ggov_submission() # to 609
    if "forms" in data:
        # change ggov forms here
        pass
    p = p.ok() # to 617

    p.contact_person = data["contact"]
    p.agree = True

    p = p.ok()
