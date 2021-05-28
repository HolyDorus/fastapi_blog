from sqlalchemy import Column, Integer, String, Text

from src.database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    body = Column(Text)
