#!/usr/bin/python3
'''
A script that uses an API and returns info
'''

import requests
from sys import argv

if __name__ == ' __main__':
        if len(argv) > 1:
                user = argv[1]
                api_url = "https://jsonplaceholder.typicode.com/"
                req_user = requests.get("{}users/{}".format(api_url, user))
                name = req_user.json().get('name')        
                if name is not None:
                        to_do = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(url, user)).json()
                        all_task = len(to_do)
                        completed_tasks = []
                        for task in to_do:
                                if task.get("completed") is True:
                                        completed_tasks.append(task)
                        completed_count = len(completed_tasks)
                        print("Employee {} is done with tasks({}/{}):".format(name, completed_count, all_task))
                        for title in completed_tasks:
                                print("\t {}".format(title.get("title")))
