import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
cat = sqlalchemy.Table('cat', metadata, autoload=True, autoload_with=engine)

#new_records = [{"name":'Kitty5', "age":2.1}, {"name":"Kitty6", "age":1.1}, {"name":"Kitty7", "age":3.1}]
#query = sqlalchemy.update(cat).values(alive=False).where(cat.columns.age > 3.1)
#query = sqlalchemy.insert(cat)
query = sqlalchemy.delete(cat).where(cat.columns.age < 1.2)
result_proxy = connection.execute(query)
#for result in result_proxy:
	#pprint(result)
