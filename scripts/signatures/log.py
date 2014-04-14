def log_signatures(p):
    # assumes that signature_count is an available method from the page
    # TODO: won't work if any signature people are blank
    count = p.signature_count
    for i in range(count):
        p = p.signature(i + 1).log()
        p.date = "1/1/08"
        p = p.ok()
    return p