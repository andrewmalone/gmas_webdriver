import re


def pagemap(page):
    """
    Maps screens from footer names to class names. In most cases this isn't needed, but some screens
    follow non-standard naming conventions or have other variations
    """
    # todo - document the reasons better!
    map = {
        "SCR0089a": "SCR0089",
        "SCR0474b": "SCR0474",
        "SCR0366v": "SCR0366",
        "SCR0005b": "SCR0005"
    }
    screen = re.search("SCR[0-9]{4}[a-z]?", page).group(0)

    # Segment home is special
    if screen == "SCR0104":
        if page == "SCR0104SegmentHome":
            screen = "SCR0104b"
        elif page == "SCR0104ProjectHome":
            screen = "SCR0104a"

    if screen in map:
        screen = map[screen]

    return screen
