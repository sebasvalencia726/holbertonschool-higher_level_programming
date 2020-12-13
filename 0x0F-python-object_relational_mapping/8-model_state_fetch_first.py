#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa.
take 3 arguments: mysql username, mysql password and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).limit(1)
    if not result:
        print("Nothing")
    for state in result:
        print('{}: {}'.format(state.id, state.name))
