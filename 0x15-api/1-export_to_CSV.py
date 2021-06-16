#!/usr/bin/python3

import csv
import requests
import sys


def save_tasks_to_csv(employee_id):
    """ """
    #set up vars
    user_name = ''
    all_tasks = []

    # get requests
    usersRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))

    # get json from requests
    user_name = usersRes.json().get('username')
    todosJson = todosRes.json()

    # file -> CSV (value,value,value...)
    for tasks in todosJson:
        task_rows = []
        task_rows.append(user_name)
        task_rows.append(tasks.get('completed'))
        task_rows.append(tasks.get('title'))

        all_tasks.append(task_rows)

    # open and write
    with open('{}.csv'.format(employee_id), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(all_tasks)

    return 0

if __name__ == '__main__':
    save_tasks_to_csv(sys.argv[1])

# specific file (ID.csv)
# all tasks for users ->
# to use the csv module
