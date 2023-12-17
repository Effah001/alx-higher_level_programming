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

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    db_name = sys.argv[3]

    dburl = f"mysql://{user_name}:{pass_word}@localhost:3306/{db_name}"

    engine = create_engine(dburl)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).all()

    for state in states:
        print(f"{state.id}: {state.name}")
