from sqlalchemy import Column, Integer, String

from db.base_class import Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
