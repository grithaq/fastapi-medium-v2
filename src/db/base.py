# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base  # noqa
from db.models.category import Category  # noqa
from db.models.user import User  # noqa
