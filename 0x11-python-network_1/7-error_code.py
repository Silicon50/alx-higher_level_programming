#!/usr/bin/python3
""" error code """
from sys import argv
from requests import get

if __name__ == "__main__":
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(request.text)
