#!/usr/bin/python3
""" Github"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    body = HTTPBasicAuth(argv[1], argv[2])
    respond = get("https://api.github.com/user", auth=body)
    print(respond.json().get('id'))
