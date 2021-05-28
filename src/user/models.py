from sqlalchemy import Column, Integer, String, DateTime, Boolean, sql

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    register_at = Column(
        DateTime(timezone=True),
        server_default=sql.func.now()
    )
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
