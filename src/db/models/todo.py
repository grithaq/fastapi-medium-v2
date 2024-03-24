from sqlalchemy import Column, ForeignKey, Integer, String

from db.base import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=True)

    def __repr__(self) -> str:
        return f"{self.title}"
