#!/usr/bin/python3
"""
This script uses REST API with an ID and returns information on todo
list progress
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_res = requests.get(url=user_url)
    user_data = user_res.json()
    username = user_data.get("username")

    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url=url)
    data = response.json()

    user_tasks = []

    for user in data:
        if user.get("userId") == int(emp_id):
            user["username"] = username
            user_tasks.append(user)

    fields = ["userId", "username", "completed", "title"]
    filename = f"{emp_id}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields, quoting=csv.QUOTE_ALL)
        for row in user_tasks:
            writer.writerow({
                key: str(value) for key, value in row.items() if key in fields
            })
