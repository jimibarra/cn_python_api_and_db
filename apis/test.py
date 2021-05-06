import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

body = {
    "id": 8,
    "userId": 90,
    "name": "testname",
    "description": "testdescription",
    "completed": "true"
       }
response = requests.put(url, json=body)
data = response.json()
print(response.status_code)
pprint(data)

