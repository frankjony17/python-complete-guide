import time
import requests as r
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
    Without parallelization, check the http status code repeatedly 
    using the interval given (in seconds). 
    Assume the request time is negligible.
"""

site = [
    {"url": "http://cnn.com", "interval": 100},
    {"url": "http://google.ca", "interval": 200},
    {"url": "http://cnn.com", "interval": 150},
    {"url": "http://httpbin.org/delay/20", "interval": 150},
    {"url": "https://www.whitehouse.gov/", "interval": 180},
    {"url": "https://abc.com/", "interval": 300},
    {"url": "https://wrongurl.xyz", "interval": 100},
    {"url": "https://pagefreezer.com", "interval": 120},
    {"url": "http://www.ycombinator.com/", "interval": 250}
]

url_request = {}


def is_available(s):
    if s["url"] in url_request:
        if url_request[s["url"]] + s["interval"] > time.time():
            return True
        return False
    return True


def make_request():
    for s in site:
        if is_available(s):
            try:
                r.get(url=s["url"], verify=False)
            except r.exceptions.RequestException:
                pass
            url_request[s["url"]] = time.time()
            print(s["url"])


make_request()
