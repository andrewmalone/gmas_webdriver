import urlparse


def url_param(url, param):
    """
    Returns the value of a given url paramater
    """
    url = urlparse.urlparse(url)
    query = urlparse.parse_qs(url.query)
    if param in query:
        return query[param][0]
    else:
        return None
