#!/usr/bin/python3
"""
This script uses REST API with an ID and returns information on todo
list progress
"""


import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/todos/{emp_id}"
    response = requests.get(url=url)
    data = response.json()
    print("""Employee {} {} done with tasks
\t {}""".format(
        data.get("id"),
        "is" if data.get("completed") else "is not",
        data.get("title")
    ))
