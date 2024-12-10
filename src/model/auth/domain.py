from pydantic import BaseModel


class Role(BaseModel):
    name: str

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    username: str
    password: str
    phone_number: str
    name: str
    last_name: str
    patronymic: str

    role_id: int

    role: Role

    class Config:
        from_attributes = True
