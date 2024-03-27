#!/usr/bin/python3
"""This script fetches data from an API to get users and their todo tasks."""

import json
import requests

if __name__ == "__main__":
    # Define the URLs for fetching data.
    employee_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    # Perform the GET requests.
    employee_list = requests.get(employee_url).json()
    todos_list = requests.get(todos_url).json()

    # Initialize an empty dictionary to hold the user data.
    user_dict = {}

    # Iterate over each employee to populate the user dictionary.
    for employee in employee_list:
        user_id = employee.get('id')
        user_dict[str(user_id)] = []

        # Go through each todo item
        for todo in todos_list:
            if todo.get('userId') == user_id:
                todos_dict = {
                    'username': employee.get('username'),
                    'task': todo.get('title'),
                    'completed': todo.get('completed')
                }
                # Append the todo task directly to the user's task list.
                user_dict[str(user_id)].append(todos_dict)

    # Print the final user dictionary.
    with open("todo_all_employees.json", "w") as file:
        json.dump(user_dict, file)
