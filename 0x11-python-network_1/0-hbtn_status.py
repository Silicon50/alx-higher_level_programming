#!/usr/bin/python3
"""get https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as respond:
        body = respond.read()

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
