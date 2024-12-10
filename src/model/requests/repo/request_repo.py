from sqlalchemy.orm import Session

from src.model.base import SQLAlchemyRepository
from src.model.requests.domain import Request
from src.model.requests.models import RequestORM


class RequestRepo(SQLAlchemyRepository[Request, RequestORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(Request, RequestORM, session)
