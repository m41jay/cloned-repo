#!/usr/bin/python3
''' task 0 module '''

import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    user = requests.get(api_url, verify=False).json()
    api_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.
    format(userId)
    todo = requests.get(api_url, verify=False).json()
    with open('{}.csv'.format(user), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
