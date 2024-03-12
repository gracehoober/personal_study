""" steps:
    open the file
    convert file from json to python dict
    logic to access certain required attributes
"""
import json

FILE_PATH = "./interview-example.json"

def all_employees():
    """ Return a list of all employees above age 30.
    >>> all_employees()
    ["Michael Brown","Robert Johnson","William Anderson","Ethan Johnson"]
    """

    # above_thirty = []
    with open(FILE_PATH) as file:
        employees = json.load(file)

        # for employee in employees:
        #     if employee["age"] != None and employee["age"] > 30:
        #         above_thirty.append(employee["name"])

        return [employee["name"] for employee in employees if employee["age"] > 30]

    # return above_thirty

def employee(position):
    """Look to see if there is an employee whose position matches the input."""

    with open(FILE_PATH) as file:
        employees = json.load(file)
        return [employee["name"] for employee in employees if employee["position"] == position]



"""Take a search term and return a list of empolyees whose first or l
ast name meets that search term"""

"""Return a count of engineers who know python"""

"""Return an empolyee's name who works on a project with wireframing
and who knowsFigma"""