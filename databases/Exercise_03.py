'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
#film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
#category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
#actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
#film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

#join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
#query = sqlalchemy.select([actor.columns.actor_id, actor.columns.first_name, actor.columns.last_name, film.columns.title]).select_from(join_statement).order_by(sqlalchemy.asc(actor.columns.actor_id))
#result_proxy = connection.execute(query)
#result_set = result_proxy.fetchall()
#pprint(result_set)

#Update all films to rental_duration 10 if length > 150
query = sqlalchemy.update(film).values(rental_duration=10).where(film.columns.length>150)
result_proxy = connection.execute(query)
query1 = sqlalchemy.select([film.columns.title, film.columns.length, film.columns.rental_duration]).select_from(film).where(film.columns.rental_duration==10).order_by(film.columns.length)
result1_proxy = connection.execute(query1)
for result1 in result1_proxy:
	pprint(result1)
