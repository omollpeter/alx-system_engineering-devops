#!/usr/bin/python3
"""
This script uses REST API with an ID and returns information on todo
list progress
"""


import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_res = requests.get(url=user_url)
    user_data = user_res.json()
    name = user_data.get("name")

    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url=url)
    data = response.json()

    user_tasks = []

    for user in data:
        if user.get("userId") == int(emp_id):
            user_tasks.append(user)
    total_tsk = len(user_tasks)
    completed = 0
    for task in user_tasks:
        if task.get("completed"):
            completed += 1

    print(f"Employee {name} is done with tasks({completed}/{total_tsk}):")
    for task in user_tasks:
        if task.get("completed"):
            print(f"\t {task.get('title')}")
