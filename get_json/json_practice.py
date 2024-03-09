"""Write vanilla flask
1. VENVS!!!! GRACE THINK!!! ENVIRONMENT THEN CODE!!!
2. install python requests with pip3 install requests
3.
4.
"""
import requests

TVMAZE_URL = "https://api.tvmaze.com/search/shows?q=startrek"
JSON_TO_MESS_WITH = None

def make_req():
    """Makes a get request to the API and returns in json and stores it in
    the global scope."""
    try:
        resp = requests.get(TVMAZE_URL)
        json = resp.json()

        global JSON_TO_MESS_WITH
        JSON_TO_MESS_WITH = json
        
    except ValueError:
        return "Issue with request or JSON"


def find_first():
    """Takes JSON and returns the first ___ value."""

def collect_names():
    """Takes JSON and returns an array of all ___ names."""