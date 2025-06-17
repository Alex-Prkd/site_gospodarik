from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import Base


class MySocialLink(Base):
    __tablename__ = "social link"

    instagram: Mapped[str] = mapped_column(String)
    telegram: Mapped[str] = mapped_column(String)