from sqlalchemy.orm import Session

from src.model.base import SQLAlchemyRepository
from src.model.requests.domain import Comment
from src.model.requests.models import CommentORM


class CommentRepo(SQLAlchemyRepository[Comment, CommentORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(Comment, CommentORM, session)
