from src.exceptions import RequestStatusDoesNotExist
from src.model.requests.domain import RequestStatus
from src.model.requests.repo.request_status_repo import RequestStatusRepo
from src.model.requests.schemes import StatusCreate, StatusUpdate


class RequestStatusService:
    def __init__(self, request_status_repo: RequestStatusRepo):
        self.request_status_repo = request_status_repo

    def get(self, obj_id: int) -> RequestStatus:
        request_status = self.request_status_repo.get(obj_id)
        if request_status is None:
            raise RequestStatusDoesNotExist(obj_id)

        return request_status

    def get_all(self) -> list[RequestStatus]:
        return self.request_status_repo.get_all()

    def create(self, obj: StatusCreate) -> RequestStatus:
        request_status = self.request_status_repo.create(obj)
        return request_status

    def update(
        self, obj_id: int, status_update: StatusUpdate
    ) -> RequestStatus:
        request_status = self.request_status_repo.get(obj_id)
        if request_status is None:
            raise RequestStatusDoesNotExist(obj_id)

        updates_status = self.request_status_repo.update(
            obj_id, status_update.model_dump(exclude_none=True)
        )

        return updates_status

    def delete(self, obj_id: int) -> None:
        request_status = self.request_status_repo.get(obj_id)
        if request_status is None:
            raise RequestStatusDoesNotExist(obj_id)

        self.request_status_repo.delete(obj_id)
