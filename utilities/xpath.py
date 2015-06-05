def text_sibling(element1, text, num, element2=None):
    if element2 is None:
        element2 = element1
    return "xpath=//%s[contains(normalize-space(text()), '%s')]/following-sibling::%s[%s]" % (element1, text, element2, num)


def text_sibling_child(element, text, num):
    return "xpath=//*[contains(normalize-space(text()), '%s')]/ancestor::td[1]/following-sibling::%s[%s]" % (text, element, num)


def parent_row_of_event(event):
    return "xpath=//a[contains(@href,'%s')]/ancestor::tr[1]" % event


if __name__ == "__main__":
    print text_sibling("td[@class='strong']", "Indirect basis", 2)
