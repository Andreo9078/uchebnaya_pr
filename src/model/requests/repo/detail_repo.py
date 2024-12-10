from sqlalchemy.orm import Session

from src.model.auth.domain import Role
from src.model.auth.models import RoleORM
from src.model.base import SQLAlchemyRepository
from src.model.requests.domain import Detail
from src.model.requests.models import DetailORM


class DetailRepo(SQLAlchemyRepository[Detail, DetailORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(Detail, DetailORM, session)
