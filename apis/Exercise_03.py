'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "testfirst",
    "last_name": "testlast",
    "email": "email@test.com"
    }
response = requests.post(url, json=body)
print(f"Status of post request is {response.status_code}.")

q_filter = {"email": "email@test.com"}
response1 = requests.get(url, params=q_filter)
pprint(response1.json())
