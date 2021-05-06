'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests
from pprint import pprint

url_users = "http://demo.codingnomads.co:8080/tasks_api/users"
url_tasks = "http://demo.codingnomads.co:8080/tasks_api/tasks"

def post_account(first, last, email):
    body = {
        "first_name": first,
        "last_name": last,
        "email": email
    }
    response = requests.post(url_users, json=body)
    return response

def view_tasks():
    response = requests.get(url_tasks)
    data = response.json()
    return data

def view_compl_tasks():
    response = requests.get(url_tasks)
    data = response.json()
    compl_list = []
    for item in data["data"]:
        if item['completed'] == True:
            compl_list.append(item)
    return compl_list

def view_incompl_tasks():
    response = requests.get(url_tasks)
    data = response.json()
    incompl_list = []
    for item in data["data"]:
        if item['completed'] == False:
            incompl_list.append(item)
    return incompl_list

def post_task(userid, name, description, completed):
    body = {
        "userId": userid,
        "name": name,
        "description": description,
        "completed": completed
    }
    response = requests.post(url_tasks, json=body)
    return response

def put_task(id, userid, name, description, completed):
    body = {
        "id": id,
        "userId": userid,
        "name": name,
        "description": description,
        "completed": completed
    }
    response = requests.put(url_tasks, json=body)
    return response

def delete_task(id):
    response = requests.delete(url_tasks + "/" + id)
    return response

message = '''
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
8) Quit
'''
message1 = "INVALID SELECTION.  Please enter a valid selection  1-8."

print(message)
while True:
    user_input = int(input("Please enter your selection 1-8:  "))
    if user_input == 1:
        input1 = input("Please enter first name: ")
        input2 = input("Please enter last name: ")
        input3 = input("Please enter email: ")
        result = post_account(input1, input2, input3)
        print(f"The status code is {result.status_code}")
        pprint(result.json())
    elif user_input == 2:
        result = view_tasks()
        print(result)
    elif user_input == 3:
        result = view_compl_tasks()
        print(result)
    elif user_input == 4:
        result = view_incompl_tasks()
        print(result)
    elif user_input == 5:
        input1 = input("Please enter user id: ")
        input2 = input("Please enter task name: ")
        input3 = input("Please enter task description: ")
        input4 = input("Please enter task completion status (true or false): ")
        result = post_task(input1, input2, input3, input4)
        print(f"The status code is {result.status_code}")
        pprint(result.json())
    elif user_input == 6:
        input1 = input("Please enter id: ")
        input2 = input("Please enter user id: ")
        input3 = input("Please enter task name: ")
        input4 = input("Please enter task description: ")
        input5 = input("Please enter task completion status (true or false): ")
        result = put_task(input1, input2, input3, input4, input5)
        print(f"The status code is {result.status_code}")
        pprint(result.json())
    elif user_input == 7:
        input1 = input("Please enter id: ")
        result = delete_task(input1)
        print(f"The status code is {result.status_code}")
    elif user_input == 8:
        break
    else:
        print(message1)
