#!/usr/bin/python3
"""
a script that lists all states
from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, State
import sys


if __name__ == "__main__":

    """
    Access the database and get the states
    """

    dburl = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1:4])

    engine = create_engine(dburl)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
