#!/usr/bin/python3
"""save all employee task info to JSON"""
import requests
import json


def export_all_to_json():
    """
    for all users/employees and all tasks, extend
    0-gather_data_from_an_API.py to export data in JSON format.
    """
    # set up vars
    usersntasks = {}
    site_string = 'https://jsonplaceholder.typicode.com/'
    ustr = site_string + 'users'
    tstr = site_string + 'todos'

    # get all json
    userJason = requests.get(ustr).json()
    todoJason = requests.get(tstr).json()

    user_info = {}

    for users in userJason:
        user_info[users['id']] = users['username']

    for tasks in todoJason:
        if usersntasks.get(tasks['userId'], False) is False:
            usersntasks[tasks['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[tasks['userId']]
        task_dict['task'] = tasks['title']
        task_dict['completed'] = tasks['completed']

        usersntasks[tasks['userId']].append(task_dict)

    # open and write
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(usersntasks, jsonFile)

    return

if __name__ == '__main__':
    export_all_to_json()
