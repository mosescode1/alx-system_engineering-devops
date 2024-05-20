#!/usr/bin/python3
"""Returns Information About A page"""
import csv
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    api_url_user_name = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_name_res = requests.get(api_url_user_name).json()

    api_url_todos = f"{api_url_user_name}/todos"

    user_todo = requests.get(api_url_todos).json()

    usr_name = user_name_res.get('username')

    csv_list = []
    for val in user_todo:
        values = [val.get('userId'), usr_name, val.get(
            "completed"), val.get("title")]
        csv_list.append(values)

    filename = f"{id}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(csv_list)
