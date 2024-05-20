#!/usr/bin/python3
"""
This script uses REST API with an ID and returns information on todo
list progress
"""


import csv
import requests


if __name__ == "__main__":
    users_info = []

    for i in range(1, 201):
        url = f"https://jsonplaceholder.typicode.com/todos/{i}"
        response = requests.get(url=url)
        data = response.json()
        users_info.append(data)

    headers = users_info[0].keys()

    with open("users.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(users_info)
