#!/usr/bin/python3
#!/usr/bin/python3
"""Returns Information About A page"""
import json
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    api_url_user_name = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_name_res = requests.get(api_url_user_name).json()

    api_url_todos = f"{api_url_user_name}/todos"

    user_todo = requests.get(api_url_todos).json()

    usr_name = user_name_res.get('username')
    filename = f"{id}.json"
    user_dict = {
        id: []
    }

    for task in user_todo:
        data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": usr_name
        }
        user_dict.get(id).append(data)

    with open(filename, mode="w", newline="") as file:
        json.dump(user_dict, file)
