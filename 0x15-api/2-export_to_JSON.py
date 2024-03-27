#!/usr/bin/python3
"""this is how to work with api to GET data"""

import csv
import json
import requests
import sys


def fetch_data(employee_url, todos_url):
    """this function to fetch data from api with POST and work with it"""
    user_list = []
    response_employee_data = requests.get(employee_url)
    employee_data = response_employee_data.json()
    employee_name = employee_data.get("username")
    id = employee_data.get("id")
    response_todos_url_data = requests.get(todos_url)
    todos_data = response_todos_url_data.json()

    for x in todos_data:
        if x.get('completed') is True:
            user_list.append(x.get("title"))
    return employee_name, id, todos_data, response_todos_url_data


def create_csv(name, id, todos_data):
    """this is function to create csv file from the output"""
    with open(f"{id}.csv", 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for x in todos_data:
            writer.writerow([f'{id}', f'{name}',
                            f"{x.get('completed')}", f"{x.get('title')}"])


def create_josn(user_id, todos_data, name):
    """Create a JSON file from the response."""
    user_dict = {str(user_id): []}
    for x in todos_data:
        task_dict = {
            "task": x.get('title'),  # No need for f-strings here.
            "completed": x.get('completed'),  # Corrected syntax.
            "username": name
        }
        user_dict[str(user_id)].append(task_dict)

    with open(f"{user_id}.json", "w") as file:
        json.dump(user_dict, file)


if __name__ == "__main__":
    id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    data = fetch_data(employee_url, todos_url)
    (employee_name, id, todos_data, response_todos_url_data) = data
    create_josn(id, todos_data, employee_name)
