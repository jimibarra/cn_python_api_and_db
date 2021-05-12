import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
dog = sqlalchemy.Table('dog', metadata, autoload=True, autoload_with=engine)

#new_records = [{"name":'Fido10', "age":2.1, "alive":True}, {"name":"Fido11", "age":1.1, "alive":True}, {"name":"Fido12", "age":3.1, "alive":False}]
#query = sqlalchemy.insert(dog).values(name="Fido9", age=1.1, alive=False)
query = sqlalchemy.delete(dog).where(dog.columns.age < 1.2)
result_proxy = connection.execute(query)
#for result in result_proxy:
	#pprint(result)
