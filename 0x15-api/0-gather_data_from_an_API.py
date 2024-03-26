#!/usr/bin/python3
"""this is how to work with api to GET data"""


import requests
import sys


def fetch_data(employee_url, todos_url):
    """this function to fetch data from api with POST and work with it"""
    user_list = []
    response_employee_data = requests.get(employee_url)
    employee_data = response_employee_data.json()
    employee_name = employee_data.get("name")
    response_todos_url_data = requests.get(todos_url)
    todos_data = response_todos_url_data.json()
    for x in todos_data:
        if x.get('completed') is True:
            user_list.append(x.get("title"))
    print(
        f"Employee {employee_name} is done with tasks("
        f"{len(user_list)}/{len(todos_data)}):"
    )
    for x in user_list:
        print(f"\t{ x}".expandtabs(4))


if __name__ == "__main__":
    """the entry point for the python code"""
    id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    fetch_data(employee_url, todos_url)
