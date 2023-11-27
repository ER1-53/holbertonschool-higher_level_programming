#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    arg = (sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine('mysql+mysqldb:\
                           //{}:{}@localhost/{}\
                           '.format(arg), pool_pre_ping=True)
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

state = session.query(State).order_by(State.id).first()
if state:
        print("{}: {}".format(state.id, state.name))
else:
    print("Nothing")

session.close()
