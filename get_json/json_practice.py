"""Write vanilla flask
1. VENVS!!!! GRACE THINK!!! ENVIRONMENT THEN CODE!!!
2. install python requests with pip3 install requests
3.
4.
"""
import requests

TVMAZE_URL = "https://api.tvmaze.com/search/shows?q=startrek"
URL = "fakeURL.com"

def make_req():
    """Makes a get request to the API and returns in json."""

    try:
        resp = requests.get(URL)
        json = resp.json()
        return json

    except ValueError:
        raise ValueError('Error in request process')


def find_first():
    """Takes JSON and returns the first show value."""

    json = make_req()
    return json[0]


def collect_names():
    """Takes JSON and returns list of all show names."""

    names = []
    json = make_req()

    print(json)
    for show_info in json:
        names.append(show_info["show"]["name"])

    return names


""" Get JSON from a file."""

def read_file(file_path, search_term):
    """Takes a file and reads it. Collects all information base
    on provided search term."""

    try:
        json = open(file_path)
        print(json)
    except FileNotFoundError:
        raise FileNotFoundError()