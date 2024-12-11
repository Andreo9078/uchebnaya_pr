from src.exceptions import RoleDoesNotExist, UserDoesNotExist
from src.model.auth.repos.role_repo import RoleRepo
from src.model.auth.repos.user_repo import UserRepo
from src.model.auth.schemes import UserCreate, UserUpdate


class UserService:
    def __init__(
        self, user_repo: UserRepo,
        role_repo: RoleRepo,
    ):
        self.user_repo = user_repo
        self.role_repo = role_repo

    def get(self, obj_id: int):
        user = self.user_repo.get(obj_id)
        if user is None:
            raise UserDoesNotExist(obj_id)

    def get_by_username(self, username: str):
        user = self.user_repo.get_by_username(username)
        if user is None:
            raise UserDoesNotExist(username)

        return user

    def get_all(self):
        return self.user_repo.get_all()

    def create(self, user_create: UserCreate):
        return self.user_repo.create(user_create.model_dump())

    def update(self, obj_id: int, user_update: UserUpdate):
        self._check_user(user_id=obj_id)
        return self.user_repo.update(
            obj_id, user_update.model_dump(exclude_none=True)
        )

    def delete(self, obj_id: int):
        self._check_user(user_id=obj_id)

        return self.user_repo.delete(obj_id)

    def _check_role(self, role_id: int) -> None:
        role = self.role_repo.get(role_id)

        if role is None:
            raise RoleDoesNotExist(role_id)

    def _check_user(self, user_id: int) -> None:
        user = self.user_repo.get(user_id)

        if user is None:
            raise UserDoesNotExist(user_id)
