from src.exceptions import RequestDoesNotExists, TechTypeDoesNotExist, RequestStatusDoesNotExist, \
    RolesMismatch, UserDoesNotExist
from src.model.auth.repos.user_repo import UserRepo
from src.model.requests.domain import Request
from src.model.requests.repo.request_repo import RequestRepo
from src.model.requests.repo.request_status_repo import RequestStatusRepo
from src.model.requests.repo.tech_type_repo import TechTypeRepo
from src.model.requests.schemes import RequestCreate, RequestUpdate


class RequestsService:
    def __init__(
        self, request_repo: RequestRepo,
        tech_type_repo: TechTypeRepo,
        status_repo: RequestStatusRepo,
        user_repo: UserRepo,
    ):
        self.request_repo = request_repo
        self.tech_type_repo = tech_type_repo
        self.status_repo = status_repo
        self.user_repo = user_repo

    def get(self, obj_id: int) -> Request:
        request = self.request_repo.get(obj_id)
        if request is None:
            raise RequestDoesNotExists(obj_id)

    def get_all(self) -> list[Request]:
        requests = self.request_repo.get_all()
        return requests

    def create(self, create_request: RequestCreate) -> Request:
        tech_type = self.tech_type_repo.get(create_request.tech_type_id)
        status = self.status_repo.get(create_request.status_id)
        master = self.user_repo.get(create_request.master_id)
        client = self.user_repo.get(create_request.client_id)

        if tech_type is None:
            raise TechTypeDoesNotExist(create_request.tech_type_id)

        if status is None:
            raise RequestStatusDoesNotExist(create_request.status_id)

        if master is None:
            raise UserDoesNotExist(create_request.master_id)
        elif master.role.name != "master":
            raise RolesMismatch(
                f"Пользователь с id {create_request.master_id} не является мастером"
            )

        if client is None:
            raise UserDoesNotExist(create_request.client_id)
        elif client.role.name != "client":
            raise RolesMismatch(
                f"Пользователь с id {create_request.client_id} не является мастером"
            )

        request = self.request_repo.create(create_request.model_dump())

        return request

    def update(self, obj_id: int, update_request: RequestUpdate) -> Request:
        request = self.request_repo.get(obj_id)
        if request is None:
            raise RequestDoesNotExists(obj_id)

        if update_request.tech_type_id is not None:
            tech_type = self.tech_type_repo.get(update_request.tech_type_id)
            if tech_type is None:
                raise TechTypeDoesNotExist(update_request.tech_type_id)

        if update_request.status_id is not None:
            status = self.status_repo.get(update_request.status_id)
            if status is None:
                raise RequestStatusDoesNotExist(update_request.status_id)

        if update_request.master_id is not None:
            master = self.user_repo.get(update_request.master_id)
            if master is None:
                raise UserDoesNotExist(update_request.master_id)
            elif master.role.name != "master":
                raise RolesMismatch(
                    f"Пользователь с id {update_request.master_id} не является мастером"
                )
        if update_request.client_id is not None:
            client = self.user_repo.get(update_request.client_id)
            if client is None:
                raise UserDoesNotExist(update_request.client_id)
            elif client.role.name != "client":
                raise RolesMismatch(
                    f"Пользователь с id {update_request.client_id} не является мастером"
                )

        return self.request_repo.update(
            obj_id, update_request.model_dump(exclude_none=True)
        )

    def delete(self, obj_id: int) -> None:
        request = self.request_repo.get(obj_id)
        if request is None:
            raise RequestDoesNotExists(obj_id)
