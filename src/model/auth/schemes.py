from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    phone_number: str
    name: str
    last_name: str
    patronymic: str

    role_id: int


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    phone_number: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    patronymic: Optional[str] = None

    role_id: Optional[int] = None


class RoleCreate(BaseModel):
    name: str


class RoleUpdate(BaseModel):
    name: str
