#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

	engine.execute("SELECT * FROM states ORDER BY states.id ASC")