#!/usr/bin/python3
"""takes url and email"""
from sys import argv
from urllib import parse
from urllib.request import Request, urlopen

if __name__ == '__main__':
    body = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = Request(argv[1], body)
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
