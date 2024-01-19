from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item table'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)

