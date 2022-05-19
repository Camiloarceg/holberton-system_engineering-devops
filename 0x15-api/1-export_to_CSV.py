#!/usr/bin/python3
""" extend your Python script to export data in the CSV format. """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    TOTAL_NUMBER_OF_TASKS = requests.get(
        "{}/todos?userId={}".format(url, argv[1])).json()
    USERNAME = requests.get(
        "{}/users/{}".format(url, argv[1])).json()["username"]
    task_list = []
    for task in TOTAL_NUMBER_OF_TASKS:
        task_list.append([argv[1], USERNAME, task["completed"], task["title"]])
    with open("{}.csv".format(argv[1]), "w") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for row in task_list:
            writer.writerow(row)
