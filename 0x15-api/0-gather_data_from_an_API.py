#!/usr/bin/python3
"""using this REST API, for a given employee ID,
   returns information about his/her todo list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    TOTAL_NUMBER_OF_TASKS = len(
        requests.get("{}/todos?userId={}".format(url, argv[1])).json())
    NUMBER_OF_DONE_TASKS = requests.get(
        "{}/todos?userId={}&completed=true".format(url, argv[1])).json()
    EMPLOYEE_NAME = requests.get(
        "{}/users/{}".format(url, argv[1])).json()["name"]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), TOTAL_NUMBER_OF_TASKS))

    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task["title"]))
