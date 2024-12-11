from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.model.auth.domain import User
from src.model.auth.models import UserORM
from src.model.base import SQLAlchemyRepository


class UserRepo(SQLAlchemyRepository[User, UserORM, int]):
    def __init__(self, session: Session) -> None:
        super().__init__(User, UserORM, session)

    def get_by_username(self, username: str) -> Optional[User]:
        statement = select(self.table).where(self.table.username == username)
        res = self.session.execute(statement)
        return res.scalar_one_or_none()
    
