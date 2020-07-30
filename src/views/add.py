import sqlalchemy as sa
from sql import data
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Family(Base):

	"""
	Describe base
	"""

	__tablename__ = "Family"

	id = sa.Column(sa.INTEGER, primary_key=True)
	name = sa.Column(sa.TEXT)
	age = sa.Column(sa.INTEGER)

	def to_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"age": self.age,
		}


engine = sa.create_engine(data)
Session = sessionmaker(engine)
session = Session()

# add = Family(name="Vyacheslav", age=32)

def db_add(json):

	add = Family(name=json['name'], age=int(json['age']))
	session.add(add)
	session.commit()

def form_list():
	base_list = session.query(Family).all()
	return base_list

def find_one_member(uid):
	member = session.query(Family).filter(Family.id == uid)
	# dict = [key.to_dict() for key in member]
	for i in member:
		dict = i.to_dict()
		if dict:
			return dict
		else:
			return 'Request is empty'

# db_inject(add)
