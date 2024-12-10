from sqlalchemy.orm import Session

from src.model.base import SQLAlchemyRepository
from src.model.requests.domain import UsedDetail
from src.model.requests.models import UsedDetailORM


class UsedDetailRepo(SQLAlchemyRepository[UsedDetail, UsedDetailORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(UsedDetail, UsedDetailORM, session)
