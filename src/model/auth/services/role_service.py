from src.exceptions import RoleDoesNotExist
from src.model.auth.domain import Role
from src.model.auth.repos.role_repo import RoleRepo
from src.model.auth.schemes import RoleCreate, RoleUpdate


class RoleService:
    def __init__(self, role_repo: RoleRepo):
        self.role_repo = role_repo

    def get(self, obj_id: int) -> Role:
        role = self.role_repo.get(obj_id)
        if role is None:
            raise RoleDoesNotExist(obj_id)

        return role

    def get_all(self) -> list[Role]:
        return self.role_repo.get_all()

    def create(self, create_role: RoleCreate) -> Role:
        role = self.role_repo.create(create_role.model_dump())
        return role

    def update(self, obj_id: int, update_role: RoleUpdate) -> Role:
        role = self.role_repo.get(obj_id)

        if role is None:
            raise RoleDoesNotExist(obj_id)

        updated_role = self.role_repo.update(
            obj_id, update_role.model_dump(exclude_none=True)
        )

        return updated_role

    def delete(self, obj_id: int) -> None:
        role = self.role_repo.get(obj_id)

        if role is None:
            raise RoleDoesNotExist(obj_id)

        self.role_repo.delete(obj_id)
    