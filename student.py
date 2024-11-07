from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqlite:///enrolment.db'

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class Enrolment(Base):
    __tablename__ = "enrolments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    module = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

with session.begin():
    new_enrolments = [
        Enrolment(name='Alice Cooper', module="Mathmatics, Data Science"),
        Enrolment(name='Robert Ludlum', module="Mathematics, Robotics"),
        Enrolment(name='Anita Kapur', module="Artificial Intelligence, Robotics" ),
        Enrolment(name='James Colburn', module="Data Science, Artificial Intelligence")
    ]
    for enrolee in new_enrolments:
       session.add(enrolee)

    session.commit()

# Commit the transaction
session.commit()

for user in session.query(Enrolment).all():
    print(f"Name: {user.name}, Module: {user.module}")