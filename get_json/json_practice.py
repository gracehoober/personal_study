""" My notes:
1. VENVS!!!! GRACE THINK!!! ENVIRONMENT THEN CODE!!!
2. install python requests with pip3 install requests
3. adding to a list is .append()
4.
"""

"""Get JSON from an API call. """
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
import json

def empolyees_search(file_path, search_term):
    """Takes a file and reads it. Collects all people base
    on provided search term."""







def all_projets(file_path):
    """Returns a list of projects"""

    projects = []
    with open(file_path) as file:
        person_list = json.load(file)
        for person in person_list:
            for project in person["projects"]:
                projects.append(project)

    return projects

def project(file_path, project_name):
    """Returns a single project based on the provided name."""

def serialize():
    """"""

def deserialize_json():
    """"""