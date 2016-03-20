def log_notice(p, data=None):
    if data is None:
        data = {
            "issued": "1/1/08",
            "received": "1/1/08"
        }
    # start from request home
    p = p.log_notice()
    p = p.ok()

    if "award_number" in data:
        p.award_number = data["award_number"]
    p.date_issued = data["issued"]
    p.date_received = data["received"]

    p = p.ok()
    return p
