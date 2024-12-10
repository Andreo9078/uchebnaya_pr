from sqlalchemy.orm import Session

from src.model.base import SQLAlchemyRepository
from src.model.requests.domain import TechType
from src.model.requests.models import TechTypeORM


class TechTypeRepo(SQLAlchemyRepository[TechType, TechTypeORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(TechType, TechTypeORM, session)
