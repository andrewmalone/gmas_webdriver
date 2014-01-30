def xpath_text_sibling(element, text, num):
    return "//%s[contains(normalize-space(text()), '%s')]/following-sibling::%s[%s]" % (element, text, element, num)