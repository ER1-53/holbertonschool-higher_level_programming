#!/usr/bin/python3
"""Start link class to table in database"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    contain_a = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id)
    for state in contain_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
