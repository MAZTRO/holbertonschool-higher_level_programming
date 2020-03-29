#!/usr/bin/python3
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":

    av = sys.argv
    engine = create_engine("mysql+mysqldb:\
//{}:{}@localhost:3306/{}".format(av[1], av[2], av[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    id_obj = session.query(State).get(2)

    id_obj.name = 'New Mexico'
    session.commit()

    session.close()
