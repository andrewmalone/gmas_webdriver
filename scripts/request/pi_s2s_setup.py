# @todo - accept data being passed in
def pi_s2s_setup(p, data):
    # do the person search
    p = p.global_header.goto_people()
    p.name = data["pi"]
    p = p.search().click_first_result()

    if p.count_phones() == 0:
        p = p.add_phone()
        p.phone_type = "Office Voice"
        p.phone = "12345"
        p = p.ok()

    if p.count_emails() == 0:
        p = p.add_email()
        p.email = "a@b.com"
        p = p.ok()

    if p.count_addresses() == 0:
        p = p.add_address()
        p.line1 = "Street 1"
        p.city = "City"
        p.state = "Maine"
        p.zip_code = "12345"
        p = p.ok()

    if p.count_credentials() == 0:
        p = p.add_credential()
        p.agency = "NIH"
        p.credential = "abcdefg"
        p = p.ok()

    p = p.global_header.goto_home()
    return p
