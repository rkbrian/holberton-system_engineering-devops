#!/usr/bin/python3

import csv
import requests
import sys


def save_tasks_to_csv(employee_id):
    """extend 0-gather_data_from_an_API.py to export data in the CSV format"""
    # set up vars
    user_name = ''
    all_tasks = []
    site_string = 'https://jsonplaceholder.typicode.com/users/'
    ustr = site_string + '{}'.format(employee_id)
    tstr = site_string + '{}/todos'.format(employee_id)

    # get requests
    usersRes = requests.get(ustr)
    todosRes = requests.get(tstr)

    # get json from requests
    user_name = usersRes.json().get('username')
    todosJson = todosRes.json()

    # file -> CSV (value,value,value...)
    for tasks in todosJson:
        task_rows = [employee_id]
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
