#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_name = 'https://jsonplaceholder.typicode.com/users'
    r_name = requests.get(url_name)
    json_name = r_name.json()
    for user in json_name:
        if (str(user.get("id")) == user_id):
            user_name = user.get("name")
    total_todos = 0
    total_completed_todos = 0
    completed_list = []
    url = 'https://jsonplaceholder.typicode.com/todos'
    r = requests.get(url)
    json = r.json()
    for todo in json:
        if (str(todo.get("userId")) == user_id):
            total_todos += 1
            if todo.get("completed"):
                total_completed_todos += 1
                completed_list.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(user_name, total_completed_todos, total_todos))
    for todo in completed_list:
        print('\t {}'.format(todo))
