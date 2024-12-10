from src.exceptions import TechTypeDoesNotExist
from src.model.requests.domain import TechType
from src.model.requests.repo.tech_type_repo import TechTypeRepo
from src.model.requests.schemes import TechTypeCreate, TechTypeUpdate


class TechTypeService:
    def __init__(self, tech_type_repo: TechTypeRepo):
        self.tech_type_repo = tech_type_repo

    def get(self, obj_id: int) -> TechType:
        tech_type = self.tech_type_repo.get(obj_id)
        if tech_type is None:
            raise TechTypeDoesNotExist(obj_id)

        return tech_type

    def get_all(self) -> list[TechType]:
        return self.tech_type_repo.get_all()

    def create(
        self, tech_type_create: TechTypeCreate
    ) -> TechType:
        tech_type = self.tech_type_repo.create(tech_type_create.model_dump())
        return tech_type

    def update(self, obj_id: int, tech_type_update: TechTypeUpdate) -> TechType:
        tech_type = self.tech_type_repo.get(obj_id)

        if tech_type is None:
            raise TechTypeDoesNotExist(obj_id)

        updated_tech_type = self.tech_type_repo.update(
            obj_id, tech_type_update.model_dump(exclude_none=True)
        )

        return updated_tech_type

    def delete(self, obj_id: int) -> None:
        tech_type = self.get(obj_id)
        if tech_type is None:
            raise TechTypeDoesNotExist(obj_id)

        self.tech_type_repo.delete(obj_id)
