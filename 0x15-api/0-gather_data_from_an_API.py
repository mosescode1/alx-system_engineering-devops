#!/usr/bin/python3
"""Returns Information About A page"""
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    api_url_user_name = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_name_res = requests.get(api_url_user_name).json()

    api_url_todos = f"{api_url_user_name}/todos"

    user_todo = requests.get(api_url_todos).json()

    emp_name = user_name_res.get('name')

    total_task = 0
    completed = 0

    for val in user_todo:
        total_task += 1
        if val.get('completed'):
            completed += 1

    print(
        f"Employee {emp_name} is done with tasks({completed}/{total_task}):")

    [print(f"\t {val.get('title')}") for val in user_todo]
