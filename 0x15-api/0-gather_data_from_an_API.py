#!/usr/bin/python3
''' task 0 module '''


import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        user = argv[1]
        api_url = 'https://jsonplaceholder.typicode.com/'
        req = requests.get('{}users/{}'.format(api_url, user))
        name = req.json().get('name')
        if name is None:
            jsn_req = requests.get(
                "{}todos?userId={}".format(
                    api_url, user)).json()
            alltask = len(jsn_req)
            completedtask = []
            for task in jsn_req:
                if task.get("completed") is True:
                    completedtask.append(task)
            completedtask_count = len(completedtask)
            print('Employee {} is done with tasks({}/{}):'
                  .format(name, completedtask_count, alltask))
            for title in completedtask:
                print('Employee {} is done with tasks({}/{}:'
                      .format(name, completedtask_count, alltask))
                for title in completedtask:
                    print('\t {}'.format(title.get('title')))
