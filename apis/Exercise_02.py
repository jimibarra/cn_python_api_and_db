'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)
data = response.json()

email_list = []
for item in data['data']:
    email = item['email']
    email_list.append(email)
print(email_list)
print(len(email_list))

