#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
from sys import argv


def export_to_csv(user_id):
    """Export to CSV"""
    user_id = argv[1]
    to_do = 'https://jsonplaceholder.typicode.com/todos/'
    users = 'https://jsonplaceholder.typicode.com/users/'
    todo_req = requests.get(to_do, params={'userId': user_id})
    user_req = requests.get(users, params={'id': user_id})
    todo_l = todo_req.json()
    user_l = user_req.json()

    name = user_l[0].get('username')
    n_file = user_id + '.csv'
    with open(n_file, 'w') as csv_file:
        tasks = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_l:
            tasks.writerow([user_id, name,
                           task.get('completed'), task.get('title')])

if __name__ == "__main__":
    export_to_csv(int(argv[1]))
