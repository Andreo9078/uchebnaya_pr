from pydantic import BaseModel

from src.model.auth.models import RoleORM


class Role(BaseModel):
    name: str


class User(BaseModel):
    id: int
    username: str
    password: str
    phone_number: str
    name: str
    last_name: str
    patronymic: str

    role_id: int

    role: RoleORM
