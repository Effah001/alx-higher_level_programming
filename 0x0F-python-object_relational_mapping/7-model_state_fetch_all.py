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
    Session = sessionmaker()
    engine = create_engine(
        "mysql://{}:{}@localhost/{}".format(*sys.argv[1:4]), pool_pre_ping=True
    )
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
