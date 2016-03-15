class Lookup(object):
    def __init__(self, input_element, name, doc=None):
        self.input = input_element
        # print type(input_element)
        self.input_locator = "css=input[onchange*='%s']" % name
        self.lookup_locator = "css=a[href*='%s'] img" % name
        self.match_locator = "css=img[name='%s'][src$='i_match.gif']" % name
        if doc != None:
            self.__doc__ = "%s%s" % (doc, self.__doc__)

    def __get__(self, obj, cls=None):
        pass


class Lookup_basic(Lookup):
    def __set__(self, obj, val):
        # set the text
        self.input.__set__(obj, val)
        # click the lookup
        obj.find_element(self.lookup_locator).click()
        # wait for a match
        obj.w.until(lambda e: obj.find_element(self.match_locator))


class Lookup_org(Lookup_basic):
    """
    Org lookup expects a 5 digit org value
    """
    pass


class Lookup_person(Lookup_basic):
    """
    Person lookup expects an 8 digit HUID
    """
    def __set__(self, obj, val):
        # check for HUID...
        import re
        if re.match(r'[0-9]{8}', val):
            # set the text
            self.input.__set__(obj, val)
            # click the lookup
            obj.find_element(self.lookup_locator).click()
            # wait for a match
            obj.w.until(lambda e: obj.find_element(self.match_locator))
        else:
            self.input.__set__(obj, val)
            obj.find_element(self.lookup_locator).click()
            obj.switch_to_popup()
            popup = obj.load_page()
            popup.select_first_non_huid()
            popup.ok()



class Lookup_organization(Lookup):
    """
    Organization lookup will match the first result in the popup
    """
    def __set__(self, obj, val):
        self.input.__set__(obj, val)
        obj.find_element(self.lookup_locator).click()
        obj.switch_to_popup()
        popup = obj.load_page()
        popup.select_first_result()
        popup.ok()

class Lookup_root(Lookup_basic):
    """
    Root lookup
    """
    pass

class Lookup_opportunity(Lookup):
    """
    Opportunity lookup (if multiple competition ids, selects the first one)
    """
    def __set__(self, obj, val):
        comp_id = None
        # check for string vs tuple
        if type(val) is tuple:
            comp_id = val[1]
            val = val[0]
        self.input.__set__(obj, val)
        obj.find_element(self.lookup_locator).click()
        obj.switch_to_popup()
        popup = obj.load_page()
        if popup.competition_count > 0:
            if comp_id is None:
                popup.select_competition(1)
            else:
                popup.competition = comp_id
        popup.ok()
        obj.w.until(lambda e: obj.find_element(self.match_locator))
