#!/usr/bin/python3
"""
a script that lists all states
from the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    dburl = "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:4])

    engine = create_engine(dburl)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state_name = sys.argv[4]

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print('{0}'.format(state.id))
    else:
        print("Not found")
