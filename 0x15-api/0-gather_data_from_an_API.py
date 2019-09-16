#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    to_do = 'https://jsonplaceholder.typicode.com/todos/'
    users = 'https://jsonplaceholder.typicode.com/users/'
    todo_req = requests.get(to_do, params={'userId': employee_id})
    user_req = requests.get(users, params={'id': employee_id})

    todo_l = todo_req.json()
    user_l = user_req.json()

    done = []
    employee = user_l[0].get('name')

    for task in todo_l:
        if task.get('completed'):
            done.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(done), len(todo_l)))

    for task in done:
        print("\t {}".format(task.get('title')))
