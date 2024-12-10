from src.exceptions import UsedDetailDoesNotExist, DetailDoesNotExist, RequestDoesNotExist
from src.model.requests.domain import UsedDetail
from src.model.requests.repo.detail_repo import DetailRepo
from src.model.requests.repo.request_repo import RequestRepo
from src.model.requests.repo.used_detail_repo import UsedDetailRepo
from src.model.requests.schemes import UsedDetailCreate, UsedDetailUpdate


class UsedDetailsService:
    def __init__(
        self, used_details_repo: UsedDetailRepo,
        detail_repo: DetailRepo,
        request_repo: RequestRepo,
    ):
        self.used_details_repo = used_details_repo
        self.detail_repo = detail_repo
        self.request_repo = request_repo

    def get(self, obj_id: int) -> UsedDetail:
        used_detail = self.used_details_repo.get(obj_id)
        if used_detail is None:
            raise UsedDetailDoesNotExist(obj_id)

        return used_detail

    def get_all(self) -> list[UsedDetail]:
        return self.used_details_repo.get_all()

    def create(self, obj_create: UsedDetailCreate) -> UsedDetail:
        detail = self.detail_repo.get(obj_create.detail_id)
        if detail is None:
            raise DetailDoesNotExist(obj_create.detail_id)

        request = self.request_repo.get(obj_create.request_id)
        if request is None:
            raise RequestDoesNotExist(obj_create.request_id)

        used_detail = self.request_repo.create(detail.model_dump())

        return used_detail

    def update(self, obj_id: int, obj_update: UsedDetailUpdate) -> UsedDetail:
        if obj_update.detail_id is not None:
            detail = self.detail_repo.get(obj_update.detail_id)
            if detail is None:
                raise DetailDoesNotExist(obj_update.detail_id)

        if obj_update.request_id is not None:
            request = self.request_repo.get(obj_update.request_id)
            if request is None:
                raise RequestDoesNotExist(obj_update.request_id)

        used_detail = self.used_details_repo.update(
            obj_id, obj_update.model_dump(exclude_none=True)
        )
        return used_detail

    def delete(self, obj_id: int) -> None:
        detail = self.detail_repo.get(obj_id)
        if detail is None:
            raise UsedDetailDoesNotExist(obj_id)
