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

    for item in emp_todos:
        total_todos += 1

        if item.get('completed') is True:
            done_todos += 1
            done_todo_titles.append(item.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        emp_name,
        done_todos,
        total_todos
    ))

    for title in done_todo_titles:
        print('\t ' + title)
