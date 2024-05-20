#!/usr/bin/python3
"""
This script uses REST API with an ID and returns information on todo
list progress then exports to JSON
"""


import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_res = requests.get(url=users_url)
    users_data = users_res.json()
    count = len(users_data)

    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url=url)
    data = response.json()

    all = {}
    for i in range(1, count + 1):
        user_tasks = []

        for user in data:
            if user.get("userId") == int(i):
                for user_info in users_data:
                    if user_info.get("id") == i:
                        user["username"] = user_info.get("username")
                user_tasks.append(user)

        task_recs = []
        for task in user_tasks:
            task = {
                "username": task.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_recs.append(task)

        all[i] = task_recs

    json_file = "todo_all_employees.json"

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(all, file)
