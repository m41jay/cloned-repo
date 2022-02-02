#!/usr/bin/python3
"""
2-export_to_JSON.py
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    file_name = str(user_id) + '.json'
    url = 'https://jsonplaceholder.typicode.com'
    url_users = url + '/users'
    url_todos = url + '/todos'
    """get user name"""
    r_user = requests.get(url_users + '/?id=' + str(user_id))
    user_username = r_user.json()[0].get("username")
    """get to-dos of a user"""
    r_todos = requests.get(url_todos + '/?userId=' + str(user_id))
    user_todos = r_todos.json()
    main_dict = {}
    task_list = []
    for todo in user_todos:
        task_dict = {}
        task_dict["task"] = todo.get("title")
        task_dict["completed"] = todo.get("completed")
        task_dict["username"] = user_username
        task_list.append(task_dict)
    main_dict["{}".format(str(user_id))] = task_list
    """add data to file"""
    with open(file_name, 'a') as f:
        f.write(json.dumps(main_dict))
