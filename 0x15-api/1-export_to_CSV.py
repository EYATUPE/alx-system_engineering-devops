#!/usr/bin/python3
""" make a request to a url and extract data """

if __name__ == '__main__':
    import requests
    from sys import argv

    emp_id = argv[1]
    total_todos = 0
    done_todos = 0
    done_todo_titles = []

    result = requests.get('https://jsonplaceholder.typicode.com/users/' +
                          emp_id)
    emp_name = result.json().get('name')

    result = requests.get('https://jsonplaceholder.typicode.com/users/' +
                          emp_id + '/todos')
    emp_todos = result.json()

    import csv
with open("USER_ID.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))
