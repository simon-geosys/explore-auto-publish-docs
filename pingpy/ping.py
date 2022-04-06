import requests

def ping(url):
    """Pings the url.

    Args:
    url : A string representing the url to ping.

    Returns:
    A String with the response status code
    """
    
    return requests.get('url').status_code
