def submit(p, data=None):
    if data is None:
        data = {
            "date_r": "1/1/08",
            "date_s": "1/1/08",
            "method": "Federal express",
            "submitted_by": "03750001"
        }
    p = p.submit()
    p.date_received = data["date_r"]
    p.date_submitted = data["date_s"]
    p.method = data["method"]
    p.submitted_by = data["submitted_by"]
    p = p.ok()
    return p


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
