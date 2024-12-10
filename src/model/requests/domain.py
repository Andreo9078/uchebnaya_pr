from datetime import datetime

from pydantic import BaseModel

from src.model.auth.domain import User


class UsedDetail(BaseModel):
    id: int
    price: float
    count: int

    detail: "Detail"
    request: "Request"

    class Config:
        from_attributes = True


class TechType(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class RequestStatus(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class Comment(BaseModel):
    id: int
    comment: str
    grade: int

    request: "Request"

    class Config:
        from_attributes = True


class Detail(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class Request(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    description: str
    tech_model: str

    tech_type: TechType
    status: RequestStatus
    master: User
    client: User
    comments: Comment
    used_details: UsedDetail

    class Config:
        from_attributes = True
