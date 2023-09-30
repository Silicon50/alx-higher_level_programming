#!/usr/bin/python3
"""A script that: takes in a URL, sends a request to the URL and displays the value
"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    with urlopen(req) as respond:
        print(dict(respond.headers).get("X-Request-Id"))
