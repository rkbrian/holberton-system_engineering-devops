#!/usr/bin/python3

import requests
import sys
import json


def export_tasks_to_json(employee_id):
    """ """
    #set up vars
    user_name = ''
    user_dict = {}

    # get requests
    usersRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))

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
