from pages.Page import Page
import utilities.xpath as xpath
from pages.elements import RText


class SCR0647(Page):
    """
    SCR_0647 Financial award information
    """
    locators = {
        "contact name": xpath.text_sibling("td", "Contact name:", 1)
    }

    _locators = {
        "contact name": "xpath=//span[@id='contactName']/.."
    }

    contact_name = RText("contact name", "Financial contact name")
