#!/usr/bin/python3
'''
A script that uses an API and returns info
'''


if __name__ == " __main__":
    import requests
    from sys import argv

    userId = argv[1]
    all_tsk = 0
    completed_tsk = 0
    completed_tsk_titles = []

    req_user = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            userId)
    name = req_user.json().get("name", "user name not found")

    req_user = requests.get("https://jsonplaceholder.typicode.comu/users/" +
                            user + "/todos")
    user_tsk = req_user.json()

    for task in user_tsk:
        all_tks += 1
        if task.get("completed") is True:
            completed_tsk += 1
            completed_tsk_titles.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(name, completed_tsk, all_tsk))
    for title in completed_tsk_title:
        print("\t {}".format(title.get("title")))
