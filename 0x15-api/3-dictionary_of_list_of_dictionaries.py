#!/usr/bin/python3
"""Dictionary of list"""
import csv
import json
import requests
from sys import argv


def dict_of_list():
    n_file = 'todo_all_employees.json'
    to_do = 'https://jsonplaceholder.typicode.com/todos/'
    users = 'https://jsonplaceholder.typicode.com/users/'
    todo_req = requests.get(to_do)
    user_req = requests.get(users)

    todo_l = todo_req.json()
    user_l = user_req.json()

    workers = {}
    current_user = {}

    for phil in user_l:
        user_id = phil.get('id')
        workers[user_id] = []
        current_user[user_id] = phil.get('username')

    for task in todo_l:
        current_task = {}
        user_id = task.get('userId')
        current_task['task'] = task.get('title')
        current_task['completed'] = task.get('completed')
        right_u = current_user.get(user_id)
        current_task['username'] = right_u
        workers.get(user_id).append(current_task)

    with open(n_file, 'w', newline='') as jsonfile:
        json.dump(workers, jsonfile)

if __name__ == "__main__":
    dict_of_list()
