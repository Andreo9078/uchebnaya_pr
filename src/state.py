from typing import Optional

from src.model.auth.domain import User


class State:
    current_user: Optional[User] = None


state = State()
