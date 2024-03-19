from sqlalchemy import Column, ForeignKey, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


category_user_table = Table(
    "category_users",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("category.id")),
    Column("user_id", Integer, ForeignKey("user.id"))
)


category_todo_table = Table(
    "category_todos",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("category.id")),
    Column("todo_id", Integer, ForeignKey("todo.id")),
)