# model/item.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    item_type = Column(String)
    unit_price = Column(Integer)
    units = Column(Integer)
