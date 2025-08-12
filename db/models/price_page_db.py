from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models import Base




class Service(Base):
    __tablename__ = "service"
    img: Mapped[str] = mapped_column(String())
    title: Mapped[str] = mapped_column(String(30))
    price: Mapped[str] = mapped_column(String())
    info: Mapped[List["InfoService"]] = relationship(back_populates="service", lazy="immediate")


class InfoService(Base):
    __tablename__ = "info_service"
    text: Mapped[str] = mapped_column(String())
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"))
    service: Mapped["Service"] = relationship(back_populates="info", lazy="immediate")


class BeforeWork(Base):
    __tablename__ = "before_work"
    title: Mapped[str] = mapped_column(String())
    info_to_work: Mapped[List["Information"]] = relationship(back_populates="work", lazy="immediate")


class Information(Base):
    __tablename__ = "info_work"
    text: Mapped[str] = mapped_column(String())
    work_id: Mapped[int] = mapped_column(ForeignKey("before_work.id"))
    work: Mapped["BeforeWork"] = relationship(back_populates="info_to_work", lazy="immediate")


# class Location(Base):
#     __tablename__ = "location"
#     text: Mapped[str] = mapped_column(String())
#
#
# class Fashion(Base):
#     __tablename__ = "fashion"
#     text: Mapped[str] = mapped_column(String())


class MyCondition(Base):
    __tablename__ = "condition"
    text: Mapped[str] = mapped_column(String())


class ConditionVideo(Base):
    __tablename__ = "condition video"
    text: Mapped[str] = mapped_column(String())


class AdditionalInfo(Base):
    __tablename__ = "additional info"
    text: Mapped[str] = mapped_column(String())


class Discount(Base):
    __tablename__ = "discount"
    text: Mapped[str] = mapped_column(String())