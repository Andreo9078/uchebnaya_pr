from sqlalchemy.orm import Session

from src.model.base import SQLAlchemyRepository
from src.model.requests.domain import RequestStatus
from src.model.requests.models import RequestStatusORM


class RequestStatusRepo(
    SQLAlchemyRepository[RequestStatus, RequestStatusORM, int]
):
    def __init__(self, session: Session) -> None:
        super().__init__(RequestStatus, RequestStatusORM, session)
