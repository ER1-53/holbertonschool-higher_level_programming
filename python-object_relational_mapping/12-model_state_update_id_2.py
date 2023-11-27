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

update_state = session.query(State).filter_by(id=2).first()

update_state.name = 'New Mexico'
session.commit()

session.close()
