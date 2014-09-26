def set(p, field, data, attr=None):
    if attr is None:
        attr = field
    if field in data:
        if hasattr(p, attr) and getattr(p, attr) is not False:
            setattr(p, attr, data[field])


def SCR0328(p, data, button):
    fields = [
        "funding_instrument",
        "payment_method",
        "loc_number",
        "arra",
        "equipment",
        "agency",
        "ia",
        "snap",
        "cfda",
        "prime",
        "org",
        "discipline",
        "foreign",
        "title",
        "pi",
        "award number"
    ]
    for field in fields:
        set(p, field, data)
    if button == "ok":
        p = p.ok()
    elif button == "next":
        p = p.next()
    return p
