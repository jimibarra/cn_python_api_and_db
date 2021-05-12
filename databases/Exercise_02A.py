import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
#film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
#film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
#category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

#join_statement = film.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
#query = sqlalchemy.select([film.columns.title, film.columns.length, category.columns.name]).select_from(join_statement)
#result_proxy = connection.execute(query)
#result_set = result_proxy.fetchall()
#pprint(result_set)

#All actors with first name Penelope
query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'Penelope')
result_proxy = connection.execute(query)
for result in result_proxy:
	pprint(result)
