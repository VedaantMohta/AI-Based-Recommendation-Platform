from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MediaType(Enum):
    MOVIE = "movie"
    BOOK = "book"
    GAME = "game"

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    media_type = Column(Enum(MediaType), nullable=False)
    rating = Column(Float, nullable=True)
    year = Column(Integer, nullable=True)