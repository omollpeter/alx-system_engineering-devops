#!/usr/bin/python3
"""
This script uses REST API with an ID and returns information on todo
list progress then exports to JSON
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

    task_recs = []
    for task in user_tasks:
        task = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": task.get("username")
        }
        task_recs.append(task)

    user_t = {emp_id: task_recs}

    json_file = f"{emp_id}.json"

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(user_t, file)
