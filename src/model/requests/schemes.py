from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DetailCreate(BaseModel):
    name: str


class DetailUpdate(BaseModel):
    name: Optional[str] = None


class CommentCreate(BaseModel):
    comment: str
    grade: int
    request_id: int


class CommentUpdate(BaseModel):
    comment: Optional[str] = None
    grade: Optional[int] = None


class TechTypeCreate(BaseModel):
    name: str


class TechTypeUpdate(BaseModel):
    name: Optional[str] = None


class StatusCreate(BaseModel):
    status: str


class StatusUpdate(BaseModel):
    status: Optional[str] = None


class RequestCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    description: str
    tech_model: str

    tech_type_id: int
    status_id: int
    master_id: int
    client_id: int


class RequestUpdate(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    description: Optional[str] = None
    tech_model: Optional[str] = None

    tech_type_id: Optional[int] = None
    status_id: Optional[int] = None
    master_id: Optional[int] = None
    client_id: Optional[int] = None


class UsedDetailCreate(BaseModel):
    price: float
    count: int
    detail_id: int
    request_id: int


class UsedDetailUpdate(BaseModel):
    price: Optional[float] = None
    count: Optional[int] = None
    detail_id: Optional[int] = None
    request_id: Optional[int] = None
