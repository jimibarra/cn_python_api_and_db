'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)
print(f"The status code is {response.status_code}.")
print(f"The encoding is {response.encoding}.")
print(f"The text is {response.text}.")

response1 = requests.get(url + "/3" )
print(f"The status code is {response1.status_code}.")
pprint(response1.json())