from sqlalchemy.orm import Session

from src.model.auth.domain import Role
from src.model.auth.models import RoleORM
from src.model.base import SQLAlchemyRepository


class RoleRepo(SQLAlchemyRepository[Role, RoleORM]):
    def __init__(self, session: Session) -> None:
        super().__init__(Role, RoleORM, session)
