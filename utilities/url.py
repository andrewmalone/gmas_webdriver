import urlparse

def url_param(url, param):
    """
    Returns the value of a given url paramater
    """
    url = urlparse.urlparse(url)
    query = urlparse.parse_qs(url.query)
    return query[param][0]