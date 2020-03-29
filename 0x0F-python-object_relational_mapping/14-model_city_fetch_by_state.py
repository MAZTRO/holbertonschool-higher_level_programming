#!/usr/bin/python3
from model_state import Base, State
from model_city import City
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

    data = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id).all()

    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
