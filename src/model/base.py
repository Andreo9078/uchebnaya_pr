from abc import ABC, abstractmethod
from typing import Iterable, Any, Type, Optional

from pydantic import BaseModel
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from src.exceptions import ObjectDoesNotExist


class RepositoryProtocol[Obj, ID](ABC):
    @abstractmethod
    def get_all(
        self, offset: int = None, limit: int = None, **filters: Any
    ) -> Iterable[Obj]: ...

    @abstractmethod
    def get(self, id_obj: ID) -> Obj: ...

    @abstractmethod
    def create(self, create_dict: dict[str, Any]) -> None: ...

    @abstractmethod
    def delete(self, id_obj: ID) -> None: ...

    @abstractmethod
    def update(self, obj: Obj, update_dict: dict[str, Any]) -> None: ...


class SQLAlchemyRepository[DomainObj: BaseModel, ORMObj, ID](
    RepositoryProtocol[ORMObj, ID]
):
    def __init__(
        self,
        domain_obj: Type[DomainObj] = BaseModel,
        table: Type[ORMObj] = None,
        session: Session = None,
    ) -> None:
        self.domain_obj = domain_obj
        self.table = table
        self.session = session

    def get(self, id_obj: ID) -> Optional[DomainObj]:
        res = self._get_orm_model(id_obj)

        if res is None:
            return None

        return self.domain_obj.model_validate(res)

    def get_all(self, **filters: Any) -> list[DomainObj]:
        stmt = self._create_get_all_stmt(**filters)
        res = self.session.execute(stmt)

        return [self.domain_obj.model_validate(scalar) for scalar in res.scalars()]

    def create(self, create_dict: dict[str, Any]) -> DomainObj:
        obj = self._create(create_dict)

        self.session.commit()
        self.session.refresh(obj)

        return self.domain_obj.model_validate(obj)

    def delete(self, id_: ID) -> DomainObj:
        obj_to_del = self._get_orm_model(id_)
        if obj_to_del:
            self.session.delete(obj_to_del)
            self.session.commit()
            return self.domain_obj.model_validate(obj_to_del)

        raise ObjectDoesNotExist(self.domain_obj.__name__, id_)

    async def update(self, id_: ID, new_values: dict[str, Any]) -> DomainObj:
        obj = await self._get_orm_model(id_)
        print(obj)
        if obj is None:
            raise ObjectDoesNotExist(self.domain_obj.__name__, id_)

        for key, value in new_values.items():
            setattr(obj, key, value)
        self.session.add(obj)

        self.session.commit()
        self.session.refresh(obj)

        return self.domain_obj.model_validate(obj)

    def _create(self, create_dict: dict[str, Any]):
        obj = self.table(**create_dict)
        self.session.add(obj)
        return obj

    def _get_orm_model(self, id_obj: ID) -> ORMObj:
        statement = select(self.table).where(self.table.id == id_obj)
        res = self.session.execute(statement)
        return res.scalar_one_or_none()

    def _create_get_all_stmt(
        self, offset: int = None, limit: int = None, **filters: Any
    ) -> Select:
        stmt = select(self.table).filter_by(**filters)
        if offset is not None:
            stmt = stmt.offset(offset)
        if limit is not None:
            stmt = stmt.limit(limit)

        return stmt
