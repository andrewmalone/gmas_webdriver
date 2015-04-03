def text_sibling(element, text, num):
    return "xpath=//%s[contains(normalize-space(text()), '%s')]/following-sibling::%s[%s]" % (element, text, element, num)


def text_sibling_child(element, text, num):
    return "xpath=//*[contains(normalize-space(text()), '%s')]/ancestor::td[1]/following-sibling::%s[%s]" % (text, element, num)


def parent_row_of_event(event):
    return "xpath=//a[contains(@href,'%s')]/ancestor::tr[1]" % event
