#!/usr/bin/python3
"""save employee task info to JSON"""
import requests
import sys
import json


def export_tasks_to_json(employee_id):
    """extend 0-gather_data_from_an_API.py to export data in JSON format"""
    # set up vars
    user_name = ''
    user_dict = {}
    site_string = 'https://jsonplaceholder.typicode.com/users/'
    ustr = site_string + '{}'.format(employee_id)
    tstr = site_string + '{}/todos'.format(employee_id)

    # get requests
    usersRes = requests.get(ustr)
    todosRes = requests.get(tstr)

    # get json from requests
    user_name = usersRes.json().get('username')
    todosJson = todosRes.json()

    user_dict[employee_id] = []

    for tasks in todosJson:
        task_dict = {}
        task_dict['task'] = tasks.get('title')
        task_dict['username'] = user_name
        task_dict['completed'] = tasks.get('completed')

        user_dict[employee_id].append(task_dict)

    # open and write
    with open('{}.json'.format(employee_id), 'w') as jsonFile:
        json.dump(user_dict, jsonFile)

    return 0

if __name__ == '__main__':
    export_tasks_to_json(sys.argv[1])
