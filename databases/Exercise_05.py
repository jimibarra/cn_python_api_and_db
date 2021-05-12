'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import requests
from pprint import pprint
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/jim")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
task = sqlalchemy.Table('task', metadata, autoload=True, autoload_with=engine)

url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
response = requests.get(url)
data = response.json()

for item in data['data']:
	query = sqlalchemy.insert(task).values(id=item['id'], userId=item['userId'], name=item['name'], description=item['description'], completed=item['completed'])
	result_proxy = connection.execute(query)
