#!/usr/bin/python3
"""Export to JSON"""
import csv
import json
import requests
from sys import argv


def export_to_json(user_id):
    user_id = argv[1]
    to_do = 'https://jsonplaceholder.typicode.com/todos/'
    users = 'https://jsonplaceholder.typicode.com/users/'
    todo_req = requests.get(to_do, params={'userId': user_id})
    user_req = requests.get(users, params={'id': user_id})

    todo_l = todo_req.json()
    user_l = user_req.json()

    name = user_l[0].get('username')
    n_file = user_id + '.json'

    done_task = []
    for fetch in todo_l:
        cur_task = {}
        cur_task['task'] = fetch.get('title')
        cur_task['completed'] = fetch.get('completed')
        cur_task['username'] = name
        done_task.append(cur_task)
    jsonify = {}
    jsonify[user_id] = done_task
    with open(n_file, 'w', newline='') as jsonfile:
        json.dump(jsonify, jsonfile)

if __name__ == "__main__":
    export_to_json(int(argv[1]))
