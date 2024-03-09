"""Write vanilla flask
1. VENVS!!!! GRACE THINK!!! ENVIRONMENT THEN CODE!!!
2. install python requests with pip3 install requests
3.
4.
"""
import requests

TVMAZE_URL = "https://api.tvmaze.com/search/shows?q=startrek"

def make_req():
    """Makes a get request to the API and returns in json."""

    try:
        resp = requests.get(TVMAZE_URL)
        json = resp.json()
        return json

    except ValueError:
        return "Issue with request or JSON"


def find_first():
    """Takes JSON and returns the first ___ value."""

def collect_names():
    """Takes JSON and returns an array of all ___ names."""