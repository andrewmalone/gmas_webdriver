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
        "SCR0005b": "SCR0005",
        "SCR0092b": "SCR0092",
        # disable confirmations use uppercase
        "SCR0602A": "SCR0602a",
        "SCR0602B": "SCR0602b",
        # segment home isn't standard
        "SCR0104P": "SCR0104a",
        "SCR0104S": "SCR0104b"
    }
    screen = re.search("SCR[0-9]{4}[a-z]?", page).group(0)
    exceptions = ["SCR0104", "SCR0602"]
    if screen in exceptions:
        screen = page[:8]
    if screen in map:
        screen = map[screen]

    return screen

if __name__ == "__main__":
    print pagemap("SCR0104SegmentHome")
