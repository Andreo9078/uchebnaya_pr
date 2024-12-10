from sqlalchemy.orm import Session

from src.model.auth.domain import User
from src.model.auth.models import UserORM
from src.model.base import SQLAlchemyRepository


class UserRepo(SQLAlchemyRepository[User, UserORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(User, UserORM, session)
    
