from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserEntity(Base):
    __tablename__ = "member"

    user_id = Column(String, primary_key=True, doc="개인정보동의내역id")
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    



