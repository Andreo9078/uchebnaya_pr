from src.exceptions import DetailDoesNotExist
from src.model.requests.domain import Detail
from src.model.requests.repo.detail_repo import DetailRepo
from src.model.requests.schemes import DetailCreate, DetailUpdate


class DetailService:
    def __init__(self, detail_repo: DetailRepo):
        self.detail_repo = detail_repo

    def get(self, obj_id: int) -> Detail:
        detail = self.detail_repo.get(obj_id)
        if detail is None:
            raise DetailDoesNotExist(obj_id)

        return detail

    def get_all(self) -> list[Detail]:
        return self.detail_repo.get_all()

    def create(self, detail_create: DetailCreate) -> Detail:
        detail = self.detail_repo.create(detail_create.model_dump())
        return detail

    def update(
        self, obj_id: int, detail_update: DetailUpdate
    ) -> Detail:
        detail = self.detail_repo.get(obj_id)

        if detail is None:
            raise DetailDoesNotExist(obj_id)

        return detail.update(detail_update.model_dump(exclude_none=True))

    def delete(self, obj_id: int) -> None:
        detail = self.detail_repo.get(obj_id)
        if detail is None:
            raise DetailDoesNotExist(obj_id)

        self.detail_repo.delete(obj_id)
