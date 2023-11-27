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

state_name = session.query(State).filter_by(name=sys.argv[4]).first()
if state_name:
    print(state_name.id)
else:
    print("Not found")

session.close()
