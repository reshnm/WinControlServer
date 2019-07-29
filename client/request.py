import requests
import json

def post(url, json_data):
    res = requests.post(url, json=json_data)
    return res

def get(url):
    res = requests.get(url)
    return res