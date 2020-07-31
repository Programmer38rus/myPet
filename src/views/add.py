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
    session.close()

def form_list():
    base_list = session.query(Family).all()
    session.close()
    return base_list


def find_one_member(uid):
    member = session.query(Family).filter(Family.id == uid)

    session.close()

    for i in member:
        dict = i.to_dict()
        if dict is not None:
            return dict
        else:
            return member


def change_member(uid, json):
    member = session.query(Family).filter(Family.id == uid).one()
    # member(name=json['name'], age=hs=json['age']))
    member.name = json['name']
    member.age = json['age']
    session.commit()
    session.close()

def delete_member(uid):
    member = session.query(Family).filter(Family.id == uid).one()

    session.delete(member)
    session.commit()
    session.close()



# change_member(1)

# db_inject(add)
