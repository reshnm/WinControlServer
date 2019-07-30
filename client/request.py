import requests
import json

def post(url, json_data):
    res = requests.post(url, json=json_data)
    return res

def get(url):
    res = requests.get(url)
    return res

def print_response(res):
    as_json = res.json()

    def do_print(m, n):
        if n in m and m[n] is not None:
            print('\n'.join(m[n].splitlines()))

    if as_json is not None:
        do_print(as_json, 'stdout')
        do_print(as_json, 'stderr')
