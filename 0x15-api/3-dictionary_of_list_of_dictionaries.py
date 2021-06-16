#!/usr/bin/python3

import requests
import json


def export_all_to_json():
    """ """
    #set up vars
    usersntasks = {}

    # get all json
    userJason = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todoJason = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_info = {}

    for users in userJason:
        user_info[users['id']] = users['username']

    for tasks in todoJason:
        if usersntasks.get(tasks['userId'], False) is False:
            # print("user added: {}".format(tasks['userId']))
            usersntasks[tasks['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[tasks['userId']]
        task_dict['task'] = tasks['title']
        task_dict['completed'] = tasks['completed']

        usersntasks[tasks['userId']].append(task_dict)

    # open and write
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(usersntasks, jsonFile)

    return 0

if __name__ == '__main__':
    export_all_to_json()
