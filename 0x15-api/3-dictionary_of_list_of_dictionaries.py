#!/usr/bin/python3
"""Returns Information About A page"""
import json
import requests
import sys


if __name__ == "__main__":

    api_url_users = f"https://jsonplaceholder.typicode.com/users"
    user_name_res = requests.get(api_url_users).json()
    i = 1
    filename = "todo_all_employees.json"
    user_dict = {}
    while i <= len(user_name_res):
        user_dict[i] = []

        users = requests.get(f"{api_url_users}/{i}").json()

        user_name = users.get("username")
        url_todo = f"{api_url_users}/{i}/todos"
        get_todo = requests.get(url_todo).json()

        for task in get_todo:
            data = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
            }
            user_dict[i].append(data)

        # print("out of the loop", i)
        i += 1

    with open(filename, mode="w", newline="") as file:
        json.dump(user_dict, file)
