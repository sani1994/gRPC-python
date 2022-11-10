from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("sqlite:///user.db", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    username = Column(String(50))
    created = Column(String(50))
    modified = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', username='%s', email='%s')>" % (
            self.name,
            self.username,
            self.email,
        )


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_user(name:str, username:str, email:str, phone_number:str)->User:
    user = User(
        name=name,
        username=username,
        email=email,
        phone_number=phone_number,
        created=str(datetime.now().timestamp()),
        modified=str(datetime.now().timestamp())
    )
    try:
        session.add(user)
        session.commit()
        return user
    except ValueError:
        raise ValueError("Data couldn't save")


def get_user(**kwargs):
    if kwargs:
        return session.query(User).filter_by(**kwargs).all()
    return session.query(User).all()


