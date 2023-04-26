import requests
import sys

# The base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# The endpoint for retrieving the employee's TODO list
TODO_ENDPOINT = "/todos?userId={}"

# The endpoint for retrieving the employee's information
USER_ENDPOINT = "/users/{}"

# The employee ID is passed as a command line argument
employee_id = int(sys.argv[1])

# Make the request to the API to retrieve the employee's TODO list
todo_response = requests.get(BASE_URL + TODO_ENDPOINT.format(employee_id))
todo_data = todo_response.json()

# Make the request to the API to retrieve the employee's information
user_response = requests.get(BASE_URL + USER_ENDPOINT.format(employee_id))
user_data = user_response.json()

# Extract the relevant data from the responses
employee_name = user_data['name']
num_done_tasks = sum(1 for task in todo_data if task['completed'])
total_tasks = len(todo_data)
done_tasks_titles = [task['title'] for task in todo_data if task['completed']]

# Print the output in the required format
print(f"Employee {employee_name} is done with {num_done_tasks}/{total_tasks} tasks:")
for title in done_tasks_titles:
    print(f"\t- {title}")
