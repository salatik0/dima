import sqlalchemy as alch
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, SmallInteger
import sqlalchemy.orm
from sqlalchemy.orm import relationship, backref


# engine = alch.create_engine("postgresql+psycopg2://salatik:salatik0506@127.0.0.1/town")
Base = alch.orm.declarative_base()


class StatsTable(Base):
    __tablename__ = "stats"
    id = Column(Integer(), primary_key=True)
    strong = Column(Integer())
    health = Column(Integer())
    gold = Column(Integer())
    speed = Column(Integer())

    print("dima")
    print("dima")
