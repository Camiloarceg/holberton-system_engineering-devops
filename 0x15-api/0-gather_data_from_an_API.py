#!/usr/bin/python3
""" using this REST API, for a given employee ID,
    returns information about his/her todo list progress
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_NAME = requests.get(f"{url}/users/{argv[1]}").json()["name"]
    NUMBER_OF_DONE_TASKS = requests.get(
        f"{url}/todos?userId={argv[1]}&completed=true").json()
    TOTAL_NUMBER_OF_TASKS = len(requests.get(
        f"{url}/todos?userId={argv[1]}").json())
    print(f"Employee {EMPLOYEE_NAME} is done with\
        tasks({len(NUMBER_OF_DONE_TASKS)}/{TOTAL_NUMBER_OF_TASKS})")
    for task in NUMBER_OF_DONE_TASKS:
        TASK_TITLE = task["title"]
        print(f"\t {TASK_TITLE}")
