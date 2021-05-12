import sqlalchemy
#from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:pwd@localhost/jim")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

task = sqlalchemy.Table('task', metadata,
				sqlalchemy.Column("id", sqlalchemy.Integer()),
				sqlalchemy.Column("userId", sqlalchemy.Integer()),
				sqlalchemy.Column("name", sqlalchemy.String(255)),
				sqlalchemy.Column("description", sqlalchemy.String(255)),
				sqlalchemy.Column("createdAt", sqlalchemy.DateTime()),
				sqlalchemy.Column("updatedAt", sqlalchemy.DateTime()),
				sqlalchemy.Column("completed", sqlalchemy.Boolean()))
metadata.create_all(engine)
