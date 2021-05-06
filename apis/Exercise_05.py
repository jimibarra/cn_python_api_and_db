'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(url +"/341")
print(f"Status of delete request is {response.status_code}.")

#q_filter = {"email": "email1@test.com"}
response1 = requests.get(url +"/341")
pprint(response1.json())
