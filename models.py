from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String, unique=True)
    meanings = relationship("Meaning", back_populates="word", cascade="all, delete-orphan")

class Meaning(Base):
    __tablename__ = 'meanings'

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey('words.id'))
    meaning = Column(String)
    word = relationship("Word", back_populates="meanings")

engine = create_engine('sqlite:///dictionary.db')
Base.metadata.create_all(engine)
