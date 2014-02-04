def text_sibling(element, text, num):
    return "xpath=//%s[contains(normalize-space(text()), '%s')]/following-sibling::%s[%s]" % (element, text, element, num)