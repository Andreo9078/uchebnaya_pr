from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, relationship

from src.database import Base
from src.model.auth.models import UserORM


class UsedDetailsORM(Base):
    __tablename__ = "used_details"
    id: Mapped[int] = Column(Integer, primary_key=True)
    detail_id: Mapped[int] = Column(Integer, ForeignKey("details.id"))
    request_id: Mapped[int] = Column(Integer, ForeignKey("requests.id"))
    price: Mapped[float] = Column(Float)
    count: Mapped[int] = Column(Integer)

    detail: Mapped["DetailORM"] = relationship("DetailORM")
    request: Mapped["RequestORM"] = relationship("RequestORM")


class TechTypesORM(Base):
    __tablename__ = "tech_types"
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True)


class RequestStatusORM(Base):
    __tablename__ = "request_statuses"
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True)


class CommentORM(Base):
    __tablename__ = "comments"
    id: Mapped[int] = Column(Integer, primary_key=True)
    comment: Mapped[str] = Column(String, nullable=True)
    grade: Mapped[int] = Column(Integer, nullable=False)

    request_id: Mapped[int] = Column(
        Integer, ForeignKey("requests.id"), nullable=False
    )

    request: Mapped["RequestORM"] = relationship(
        "RequestORM", back_populates="comments"
    )


class DetailORM(Base):
    __tablename__ = "details"
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True)


class RequestORM(Base):
    __tablename__ = "requests"
    id: Mapped[int] = Column(Integer, primary_key=True)
    start_date: Mapped[datetime] = Column(DateTime)
    end_date: Mapped[datetime] = Column(DateTime)
    description: Mapped[str] = Column(String)
    tech_model: Mapped[str] = Column(String)

    tech_type_id: Mapped[int] = Column(
        ForeignKey("org_tech_types.id"), nullable=False
    )
    status_id: Mapped[int] = Column(
        ForeignKey("request_statuses.id"), nullable=False
    )
    master_id: Mapped[int] = Column(
        ForeignKey("users.id"), nullable=True
    )
    client_id: Mapped[int] = Column(
        ForeignKey("users.id"), nullable=False
    )

    tech_type: Mapped[TechTypesORM] = relationship(TechTypesORM)
    status: Mapped[RequestStatusORM] = relationship(RequestStatusORM)
    master: Mapped[UserORM] = relationship("UserORM", foreign_keys=[master_id])
    client: Mapped[UserORM] = relationship("UserORM", foreign_keys=[client_id])
    comments: Mapped[CommentORM] = relationship(
        "CommentORM", back_populates="request"
    )
    used_details: Mapped[UsedDetailsORM] = relationship(
        "UsedDetailsORM", back_populates="request"
    )
