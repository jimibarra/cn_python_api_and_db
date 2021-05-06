'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 341,
    "first_name": "test1first",
    "last_name": "test1last",
    "email": "email1@test.com"
    }
response = requests.put(url, json=body)
print(f"Status of put request is {response.status_code}.")

#q_filter = {"email": "email@test.com"}
response1 = requests.get(url + "/341")
pprint(response1.json())