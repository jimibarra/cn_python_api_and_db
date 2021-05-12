import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
#film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
#category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([actor.columns.actor_id, actor.columns.first_name, actor.columns.last_name, film.columns.title]).select_from(join_statement).order_by(sqlalchemy.asc(actor.columns.actor_id))
#result_proxy = connection.execute(query)
#result_set = result_proxy.fetchall()
#pprint(result_set)

#All actors and the films they have been in
result_proxy = connection.execute(query)
for result in result_proxy:
	pprint(result)
