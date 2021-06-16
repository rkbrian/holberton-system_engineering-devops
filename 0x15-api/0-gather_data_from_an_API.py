#!/usr/bin/python3

import sys
import requests
import urllib

def get_employee_tasks(employee_id):
    """ """
    # set up vars
    name = ''
    task_list = []
    completed_counter = 0

    # get requests
    usersRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))

    # get json from requests
    name = usersRes.json().get('name')
    # print('Name: {}'.format(name))

    todosJson = todosRes.json()
    # print('todosJson: {}'.format(todosJson))

    for tasks in todosJson:
        if tasks.get('completed') is True:
            completed_counter += 1
            task_list.append(tasks.get('title'))
    # print('task_list: {}'.format(task_list))

    print('Employee {} is done with tasks ({}/{}):'.format(name, completed_counter, len(todosJson)))
    for ttl in task_list:
        print('\t {}'.format(ttl))
    return 0

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
