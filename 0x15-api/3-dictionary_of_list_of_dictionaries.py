#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests
import sys


def get_todos(user_id, user_username):
    """get to-dos of a user"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    r_todos = requests.get(url + '/?userId=' + str(user_id))
    user_todos = r_todos.json()
    task_list = []
    for todo in user_todos:
        task_dict = {}
        task_dict["task"] = todo.get("title")
        task_dict["completed"] = todo.get("completed")
        task_dict["username"] = user_username
        task_list.append(task_dict)
    return (task_list)


if __name__ == "__main__":
    file_name = 'todo_all_employees.json'
    main_dict = {}
    url = 'https://jsonplaceholder.typicode.com/users'
    """get all users"""
    r_users = requests.get(url)
    all_users = r_users.json()
    for user in all_users:
        user_task_list = get_todos(user.get("id"), user.get("username"))
        main_dict[str(user.get("id"))] = user_task_list
    """add data to file"""
    with open(file_name, 'a') as f:
        f.write(json.dumps(main_dict))
