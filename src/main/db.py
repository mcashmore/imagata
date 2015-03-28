'''
Created on 16 Mar 2015

@author: Michelle Cashmore
'''

# http://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know

from __builtin__ import True

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Image( Base ):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String, nullable=False)
    subcategory = Column(String)
    filename = Column(String, nullable=False,unique=True )
    author = Column(String)
    source = Column(String)
    description = Column(String)
    tags = relationship("Tag", backref="image")

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_id = Column(Integer, ForeignKey('image.id'))
    
engine = create_engine('sqlite:///sqlalchemy_example.db')