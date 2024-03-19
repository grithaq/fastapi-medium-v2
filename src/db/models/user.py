from sqlalchemy import Boolean, Column, Integer, String, Table, ForeignKey

from db.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)


user_todo_table = Table(
    "user_todos",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("todo_id", Integer, ForeignKey("todo.id"))
)


user_categories_table = Table(
    "user_categories",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("category_id", Integer, ForeignKey("category.id")),
)