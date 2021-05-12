import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

cat = sqlalchemy.Table('cat', metadata,
				sqlalchemy.Column("id", sqlalchemy.Integer()),
				sqlalchemy.Column("name", sqlalchemy.String(20), nullable=False),
				sqlalchemy.Column("age", sqlalchemy.Float(), default=3.5),
				sqlalchemy.Column("alive", sqlalchemy.Boolean(), default=True))
metadata.create_all(engine)

