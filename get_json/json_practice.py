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
    """Takes a file and reads it. Returns true if search term is found,
     else returns false
     """

    with open(file_path) as file:
        data = json.load(file)
        flattened_data = flatten(data)
        return True if search_term in flattened_data else False



def flatten(data):
    """Takes JSON structure and returns a list of all values in the structure
        like: [{'cat': 'james', 'dog': 'marty'}, {'cow': 'spot'}]
                        -> ['cat', 'james', 'dog', 'marty', 'cow', 'spot']
    """
    stack = [data]
    list_of_vals = []

    while(len(stack) > 0):
        last = len(stack) - 1
        item = stack[last]
        stack.pop()

        if isinstance(item,list) is False and isinstance(item,dict) is False:
            list_of_vals.append(item)
        else:
            if isinstance(item, dict):
                for (key, val) in item.items():
                    list_of_vals.append(key)
                    list_of_vals.append(val)
            else:
                for val in item:
                    stack.append(val)


    return set(list_of_vals)


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