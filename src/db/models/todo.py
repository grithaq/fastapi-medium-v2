from sqlalchemy import Column, ForeignKey, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


todo_user_table = Table(
    "todo_users",
    Base.metadata,
    Column("todo_id", Integer, ForeignKey("todo.id")),
    Column("user_id", Integer, ForeignKey("user.id")),
)


todo_category_table = Table(
    "todo_categories",
    Base.metadata,
    Column("todo_id", Integer, ForeignKey("todo.id")),
    Column("category_id", Integer, ForeignKey("category.id")),

)