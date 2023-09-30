#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
from requests import get

if __name__ == '__main__':
    respond = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(respond.text))
    print('\t- content:', respond.text)
